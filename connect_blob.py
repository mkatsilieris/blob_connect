"""Authenticate with Azure using environment variables and Azure AD credentials, list folders in a specified blob container, and download a specific blob file to the local machine.

Required environment variables (set in a .env file or exported):
- RESOURCE_GROUP_NAME: Name of the Azure resource group
- AZURE_STORAGE_ACCOUNT_NAME: Name of the Azure storage account
- AZURE_CONTAINER: Name of the blob container
- AZURE_TENANT_ID: Azure AD tenant ID
- AZURE_CLIENT_ID: Azure AD application (client) ID
- AZURE_CLIENT_SECRET: Azure AD application secret
- AZURE_SUBSCRIPTION_ID: Azure subscription ID

The script will:
1. Authenticate using Azure AD credentials.
2. Retrieve the storage account key.
3. List the top-level folders in the specified blob container.
4. Download a specific blob (hardcoded in the script) to 'downloaded_file.docx'.
"""

import os

from azure.identity import ClientSecretCredential
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv


def _required_env(name: str) -> str:
    """Return the value of ``name`` or raise an error if not set."""

    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Missing required environment variable: {name}")
    return value


def main() -> None:
    """Authenticate and download the target blob."""

    # Load environment variables
    load_dotenv()

    resourse_group_name = _required_env("RESOURCE_GROUP_NAME")
    account_name = _required_env("AZURE_STORAGE_ACCOUNT_NAME")
    container_name = _required_env("AZURE_CONTAINER")

    # Azure AD and subscription details
    tenant_id = _required_env("AZURE_TENANT_ID")
    client_id = _required_env("AZURE_CLIENT_ID")
    client_secret = _required_env("AZURE_CLIENT_SECRET")
    subscription_id = _required_env("AZURE_SUBSCRIPTION_ID")


    # Set environmental variables

    # Authenticate using ClientSecretCredential
    cred = ClientSecretCredential(tenant_id, client_id, client_secret)

    # Initialize the StorageManagementClient
    storage_mgmt = StorageManagementClient(cred, subscription_id)

    # Replace 'MyRG' and 'mystorageacct' with your resource group and storage account name
    keys = storage_mgmt.storage_accounts.list_keys(resourse_group_name, account_name)
    account_key = keys.keys[0].value  # Retrieve the first account key

    print("Account key:", account_key)

    # Generate connection string
    connection_string = (
        f"DefaultEndpointsProtocol=https;"
        f"AccountName={account_name};"
        f"AccountKey={account_key};"
        f"EndpointSuffix=core.windows.net"
    )

    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(
        conn_str=connection_string
    )

    container_client = blob_service_client.get_container_client(container_name)
    print(f"Folders in container '{container_name}':")
    folders = set()

    for blob in container_client.list_blobs():
        if "/" in blob.name:
            folders.add(blob.name.split("/")[0])

    for folder in sorted(folders):
        print(folder)

    blob_name = "Cards/J10_001_2024-ΥΠΟΒΟΛΗ ΑΙΤΗΣΗΣ POS ACQUIRING_WF.docx"
    blob_client = container_client.get_blob_client(blob_name)
    print(f"Downloading blob: {blob_name}")
    with open("downloaded_file.docx", "wb") as file:
        file.write(blob_client.download_blob().readall())

    print("File downloaded as 'downloaded_file.docx'")


if __name__ == "__main__":
    main()

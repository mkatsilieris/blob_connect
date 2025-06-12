"""Download a specific blob from Azure Blob Storage.

The script expects the following environment variables to be defined:

```
AZURE_TENANT_ID
AZURE_CLIENT_ID
AZURE_CLIENT_SECRET
AZURE_STORAGE_ACCOUNT_NAME
AZURE_CONTAINER
```

The variables can be placed in a ``.env`` file or exported in the
environment prior to running the script.
"""

import os

from azure.identity import ClientSecretCredential
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

    load_dotenv()

    tenant_id = _required_env("AZURE_TENANT_ID")
    client_id = _required_env("AZURE_CLIENT_ID")
    client_secret = _required_env("AZURE_CLIENT_SECRET")
    account_name = _required_env("AZURE_STORAGE_ACCOUNT_NAME")
    container_name = _required_env("AZURE_CONTAINER")

    # Authenticate using the service principal
    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )

    # Create BlobServiceClient
    blob_service_client = BlobServiceClient(
        account_url=f"https://{account_name}.blob.core.windows.net",
        credential=credential,
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

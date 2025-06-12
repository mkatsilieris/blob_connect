import os
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
AZURE_STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")

# Debug: Print environment variables (without sensitive data)
print(f"AZURE_TENANT_ID: {AZURE_TENANT_ID}")
print(f"AZURE_CLIENT_ID: {AZURE_CLIENT_ID}")
print(f"AZURE_CLIENT_SECRET: {'***' if AZURE_CLIENT_SECRET else None}")
print(f"AZURE_STORAGE_ACCOUNT_NAME: {AZURE_STORAGE_ACCOUNT_NAME}")
print(f"AZURE_CONTAINER: {AZURE_CONTAINER}")
print("-" * 50)

# Authenticate using service principal
credential = ClientSecretCredential(
    tenant_id=AZURE_TENANT_ID,
    client_id=AZURE_CLIENT_ID,
    client_secret=AZURE_CLIENT_SECRET
)

# Create BlobServiceClient
blob_service_client = BlobServiceClient(
    account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net",
    credential=credential
)

# List and print folder names in the container
container_client = blob_service_client.get_container_client(AZURE_CONTAINER)
print(f"Folders in container '{AZURE_CONTAINER}':")
folders = set()

blobs = container_client.list_blobs()

for blob in blobs:
    if '/' in blob.name:
        folder_name = blob.name.split('/')[0]
        folders.add(folder_name)

for folder in sorted(folders):
    print(folder)

# Read and download a specific file from the container
blob_name = "Cards/J10_001_2024-ΥΠΟΒΟΛΗ ΑΙΤΗΣΗΣ POS ACQUIRING_WF.docx"
blob_client = container_client.get_blob_client(blob_name)

# Download the blob content
print(f"Downloading blob: {blob_name}")
with open("downloaded_file.docx", "wb") as file:
    file.write(blob_client.download_blob().readall())

print("File downloaded as 'downloaded_file.docx'")

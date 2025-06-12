# Blob Connect

A simple script to download a file from Azure Blob Storage using a service principal.

## Requirements

- Python 3.8+
- The packages listed in `requirements.txt`.

## Setup

1. Create a `.env` file with the following variables:

   ```
   AZURE_TENANT_ID=<your-tenant-id>
   AZURE_CLIENT_ID=<your-client-id>
   AZURE_CLIENT_SECRET=<your-client-secret>
   AZURE_STORAGE_ACCOUNT_NAME=<your-storage-account>
   AZURE_CONTAINER=<your-container-name>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python connect_blob.py
   ```

The script lists the folders in the specified container and downloads a pre-defined
blob called `Cards/J10_001_2024-ΥΠΟΒΟΛΗ ΑΙΤΗΣΗΣ POS ACQUIRING_WF.docx` into
`downloaded_file.docx`.

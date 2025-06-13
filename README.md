# Blob Connect

A simple script to download a file from Azure Blob Storage using a service principal.

## Requirements

- Python 3.8+
- The packages listed in `requirements.txt`.

## Setup

1. Create a `.env` file with the following variables:

   ```env
   AZURE_STORAGE_ACCOUNT_NAME=<your-storage-account>
   AZURE_STORAGE_ACCOUNT_KEY=<your-storage-account-key>
   AZURE_CONTAINER=<your-container-name>
   RESOURCE_GROUP_NAME=<your-resource-group-name>
   AZURE_TENANT_ID=<your-tenant-id>
   AZURE_CLIENT_ID=<your-client-id>
   AZURE_CLIENT_SECRET=<your-client-secret>
   AZURE_SUBSCRIPTION_ID=<your-subscription-id>
   ```

   - `AZURE_STORAGE_ACCOUNT_NAME`: The name of your Azure Storage account.
   - `AZURE_STORAGE_ACCOUNT_KEY`: The key for your Azure Storage account.
   - `AZURE_CONTAINER`: The name of the container in your Azure Storage account.
   - `RESOURCE_GROUP_NAME`: The name of the Azure resource group containing the storage account.
   - `AZURE_TENANT_ID`: The tenant ID for Azure Active Directory.
   - `AZURE_CLIENT_ID`: The client ID for Azure Active Directory.
   - `AZURE_CLIENT_SECRET`: The client secret for Azure Active Directory.
   - `AZURE_SUBSCRIPTION_ID`: The subscription ID for your Azure account.

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

## License

This project is licensed under the MIT License. See the LICENSE file for details.

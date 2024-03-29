import os, uuid, sys
import datetime
import time
from azure.storage.blob import BlockBlobService, PublicAccess

# ---------------------------------------------------------------------------------------------------------
# Method that creates a test file in the 'Documents' folder.
# This sample application creates a test file, uploads the test file to the Blob storage,
# lists the blobs in the container, and downloads the file with a new name.
# ---------------------------------------------------------------------------------------------------------
# Documentation References:
# Associated Article - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
# What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/
# Getting Started with Blobs-https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
# Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx
# Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx
# ----------------------------------------------------------------------------------------------------------
datetime_current = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
current_time = str(datetime_current)

def run_sample():
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='adladandiag', account_key='PLkDD//pOQDCbJ/EzzAzfszFrLuj2RzpFkssg95IHIgmw1aY38/y0u81q1Ux6DJcp9t6XHHNnAy3WBcutIaTUg==')

        # Create a container called 'netmon-capture-logs'.
        container_name ='netmon-capture-logs'

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Create a file in Documents to test the upload and download.
        local_path=os.path.expanduser("C:\Network Traces\*")
        local_file_name ="test.cap"
        full_path_to_file =os.path.join(local_path, local_file_name)

        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + local_file_name)

        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()

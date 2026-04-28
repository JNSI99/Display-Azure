import os
from azure.storage.blob import BlobServiceClient

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

if not connection_string:
    raise RuntimeError("Falta AZURE_STORAGE_CONNECTION_STRING")

container_name = "my-blob"

# Carpeta donde está este script/app.py
download_path = os.path.dirname(os.path.abspath(__file__))

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)


def download_all_blobs():
    print(f"Descargando datos en: {download_path}")

    for blob in container_client.list_blobs():
        blob_name = blob.name

        # Descarga plana: ignora carpetas del blob
        file_name = os.path.basename(blob_name)

        if not file_name:
            continue

        local_file_path = os.path.join(download_path, file_name)

        blob_client = container_client.get_blob_client(blob_name)

        with open(local_file_path, "wb") as file:
            file.write(blob_client.download_blob().readall())

        print(f"Descargado: {file_name}")


if __name__ == "__main__":
    download_all_blobs()
    print("Descarga completa")
    
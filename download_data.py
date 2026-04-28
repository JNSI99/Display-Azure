import os
from azure.storage.blob import BlobServiceClient

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

if not connection_string:
    raise RuntimeError("Falta AZURE_STORAGE_CONNECTION_STRING")

container_name = "jimmy-data-raw"

# 📁 Carpeta destino (plana)
download_path = os.path.dirname(os.path.abspath(__file__))

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)


def download_all_blobs():
    print("📥 Descargando blobs (modo plano)...")

    for blob in container_client.list_blobs():
        blob_name = blob.name

        # 👇 SOLO el nombre del archivo (sin carpetas)
        file_name = os.path.basename(blob_name)

        local_file_path = os.path.join(download_path, file_name)

        blob_client = container_client.get_blob_client(blob_name)

        try:
            with open(local_file_path, "wb") as file:
                file.write(blob_client.download_blob().readall())

            print(f"⬇️ {file_name}")

        except Exception as e:
            print(f"❌ Error con {blob_name}: {e}")


if __name__ == "__main__":
    download_all_blobs()
    print("✅ Descarga completa")
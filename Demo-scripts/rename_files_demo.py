import os

carpeta = "archivos_demo"  # Cambia por tu carpeta
nuevo_prefijo = "documento_demo"

for i, archivo in enumerate(os.listdir(carpeta), start=1):
    extension = os.path.splitext(archivo)[1]
    nuevo_nombre = f"{nuevo_prefijo}_{i}{extension}"
    os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nuevo_nombre))

print("Archivos renombrados (demo).")

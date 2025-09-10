import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"  # API de prueba
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df.to_csv("datos_api_demo.csv", index=False)

print("Datos de API guardados en CSV (demo).")

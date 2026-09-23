import requests

class ServidorEmbeddings():


	def __init__(self, url):
		self.url = url


	def llamada_servidor(self, texto):
		respuesta = requests.post(
			f"{self.url}/v1/embeddings",
			json={"input": texto},
			timeout=120
		)

		respuesta.raise_for_status()
		datos = respuesta.json()
		return datos["data"][0]["embedding"]


	def generar_embeddings(self, fragmentos):
		embeddings = []

		for i, fragmento in enumerate(fragmentos, start=1):
			embedding = self.llamada_servidor(fragmento)
			embeddings.append(embedding)

			if i % 10 == 0:
				print(f"Embeddings procesados: {i}/{len(fragmentos)}")

		if len(fragmentos) % 10 != 0:
			print(f"Embeddings procesados: {len(fragmentos)}/{len(fragmentos)}")

		return embeddings
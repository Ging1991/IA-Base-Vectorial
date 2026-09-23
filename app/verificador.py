import json
import faiss


class Verificador:

	def __init__(self, ruta_configuracion):
		self.ruta_configuracion = ruta_configuracion


	def revisar_configuracion(self):
		try:
			with open(self.ruta_configuracion, "r", encoding="utf-8") as archivo:
				configuracion = json.load(archivo)
		except FileNotFoundError:
			print(f"No se encontró el archivo de configuración: {self.ruta_configuracion}")
			return

		print("Configuración cargada:")
		for clave, valor in configuracion.items():
			print(f"{clave}: {valor}")


	def revisar_base_vectorial(self, ruta_faiss, ruta_json):
		try:
			indice = faiss.read_index(ruta_faiss)
		except Exception:
			print(f"No se encontró la base vectorial: {ruta_faiss}")
			return

		try:
			with open(ruta_json, "r", encoding="utf-8") as archivo:
				documentos = json.load(archivo)
		except Exception:
			print(f"No se encontró el archivo de documentos: {ruta_json}")
			return

		print("Base vectorial:")
		print(f"Vectores: {indice.ntotal}")
		print(f"Dimensión: {indice.d}")
		print(f"Fragmentos: {len(documentos)}")
import faiss
import json

class Almacenamiento:


	def __init__(self, ruta_json, ruta_faiss):
		self.ruta_json = ruta_json
		self.ruta_faiss = ruta_faiss


	def guardar_json(self, datos):
		with open(self.ruta_json, "w", encoding="utf-8") as archivo:
			json.dump(datos, archivo, ensure_ascii=False, indent=2)


	def guardar_faiss(self, datos):
		faiss.write_index(datos, self.ruta_faiss)

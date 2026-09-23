class Vectorizador():

	def __init__(self, lector, servidor, estrategia, almacenamiento, base_vectorial):
		self.lector = lector
		self.servidor = servidor
		self.estrategia = estrategia
		self.almacenamiento = almacenamiento
		self.base_vectorial = base_vectorial

	def procesar(self):
		texto = self.lector.extraer_texto()
		fragmentos = self.estrategia.dividir_texto(texto)
		embeddings = self.servidor.generar_embeddings(fragmentos)
		vectores = self.base_vectorial.crear_indice(embeddings)
		self.almacenamiento.guardar_json(fragmentos)
		self.almacenamiento.guardar_faiss(vectores)
		print(f"Vectores almacenados en FAISS: {vectores.ntotal}")
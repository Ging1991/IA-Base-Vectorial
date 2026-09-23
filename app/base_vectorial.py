import faiss
import numpy as np

class BaseVectorial():

	def crear_indice(self, embeddings):
		vectores = np.array(embeddings, dtype="float32")
		dimension = vectores.shape[1]
		indice = faiss.IndexFlatL2(dimension)
		indice.add(vectores)
		return indice
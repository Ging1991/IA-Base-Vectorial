import json
from app.vectorizador import Vectorizador
from app.lector_pdf import LectorPDF
from app.servidor_embeddings import ServidorEmbeddings
from app.estrategia import Estrategia
from app.almacenamiento import Almacenamiento
from app.base_vectorial import BaseVectorial
from app.verificador import Verificador

CONFIGURACION = "configuracion.json"
MENU = """
Asistente para la creación de una base vectorial. Seleccione una opción.
1 - Crear base vectorial con la configuración actual.
2 - Revisar configuración actual.
3 - Revisar base vectorial actual.
"""

def crear_vectorizador(configuracion):
	lector = LectorPDF(configuracion["ruta_pdf"])
	servidor = ServidorEmbeddings(configuracion["url_servidor_embeddings"])
	estrategia = Estrategia(configuracion["longitud"], configuracion["solapamiento"])
	almacenamiento = Almacenamiento(configuracion["salida_documentos"],	configuracion["salida_faiss"])
	base_vectorial = BaseVectorial()
	return Vectorizador(lector,	servidor, estrategia, almacenamiento, base_vectorial)


def main():
	print(MENU)
	opcion = input("Seleccione una opción: ")
	verificador = Verificador(CONFIGURACION)
	with open(CONFIGURACION, "r", encoding="utf-8") as archivo:
		configuracion = json.load(archivo)

	if opcion == "1":
		vectorizador = crear_vectorizador(configuracion)
		vectorizador.procesar()

	elif opcion == "2":
		verificador.revisar_configuracion()

	elif opcion == "3":
		verificador.revisar_base_vectorial(configuracion["salida_faiss"],	configuracion["salida_documentos"])

	else:
		print("Opción no válida.")


if __name__ == "__main__":
	main()
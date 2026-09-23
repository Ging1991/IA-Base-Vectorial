from pypdf import PdfReader
import re

class LectorPDF:


	def __init__(self, ruta):
		self.ruta = ruta


	def extraer_texto(self):
		texto = self.leer_datos()
		return self.limpiar_datos(texto)


	def leer_datos(self):
		lector = PdfReader(self.ruta)
		texto = ""

		for pagina in lector.pages:
			contenido = pagina.extract_text()
			if contenido:
				texto += contenido + "\n"

		return texto


	def limpiar_datos(self, texto):
		texto = texto.replace("\n", " ")
		texto = re.sub(r"\s+", " ", texto)
		return texto.strip()

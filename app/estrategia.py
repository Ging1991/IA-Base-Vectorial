class Estrategia:


	def __init__(self, longitud, solapamiento):
		self.longitud = longitud
		self.solapamiento = solapamiento
		if longitud <= 0:
			raise ValueError("longitud debe ser mayor que 0.")
		if solapamiento < 0:
			raise ValueError("solapamiento no puede ser negativo.")
		if solapamiento >= longitud:
			raise ValueError("solapamiento debe ser menor que longitud.")


	def dividir_texto(self, texto):
		fragmentos = []
		inicio = 0
		while inicio < len(texto):
			fin = inicio + self.longitud
			fragmentos.append(texto[inicio:fin])
			inicio = fin - self.solapamiento
		return fragmentos

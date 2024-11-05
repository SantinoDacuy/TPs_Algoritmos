from cola import Cola

class ArbolBinario:

	class __Nodo:
		def __init__(self, valor, izquierda=None, derecha=None, otro_valor=None):
			self.valor = valor
			self.izquierda = izquierda
			self.derecha = derecha
			self.otro_valor = otro_valor
			self.peso = 0
	
	def __init__(self):
		self.raiz = None
	
	def peso(self, raiz):
		if raiz is None:
			return -1
		else:
			return raiz.peso
	
	def actualizar_peso(self, raiz):
		if raiz is not None:
			raiz.peso = max(self.peso(raiz.izquierda), self.peso(raiz.derecha)) + 1
	
	def rotacion_simple(self, raiz, control):
		if control:
			aux = raiz.izquierda
			raiz.izquierda = aux.derecha
			aux.derecha = raiz
		else:
			aux = raiz.derecha
			raiz.derecha = aux.izquierda
			aux.izquierda = raiz
		self.actualizar_peso(raiz)
		self.actualizar_peso(aux)
		raiz = aux
		return raiz
	
	def rotacion_doble(self, raiz, control):
		if control:
			raiz.izquierda = self.rotacion_simple(raiz.izquierda, False)
			raiz = self.rotacion_simple(raiz, True)
		else:
			raiz.derecha = self.rotacion_simple(raiz.derecha, True)
			raiz = self.rotacion_simple(raiz, False)
		return raiz
	
	def balanceo(self, raiz):
		if raiz is not None:
			if self.peso(raiz.izquierda) - self.peso(raiz.derecha) == 2:
				if self.peso(raiz.izquierda.izquierda) >= self.peso(raiz.izquierda.derecha):
					raiz = self.rotacion_simple(raiz, True)
				else:
					raiz = self.rotacion_doble(raiz, True)
			elif self.peso(raiz.derecha) - self.peso(raiz.izquierda) == 2:
				if self.peso(raiz.derecha.derecha) >= self.peso(raiz.derecha.izquierda):
					raiz = self.rotacion_simple(raiz, False)
				else:
					raiz = self.rotacion_doble(raiz, False)
		return raiz
	
	def insertar_nodo(self, valor, otro_valor=None):
		def __insertar(raiz, valor, otro_valor=None):
			if raiz is None:
				return ArbolBinario.__Nodo(valor, otro_valor=otro_valor)
			elif valor < raiz.valor:
				raiz.izquierda = __insertar(raiz.izquierda, valor, otro_valor)
			else:
				raiz.derecha = __insertar(raiz.derecha, valor, otro_valor)
			raiz = self.balanceo(raiz)
			self.actualizar_peso(raiz)
			return raiz
		
		self.raiz = __insertar(self.raiz, valor, otro_valor)
	
	def busqueda(self, clave):
		def __buscar(raiz, clave):
			if raiz is not None:
				if raiz.valor == clave:
					return raiz
				elif clave < raiz.valor:
					return __buscar(raiz.izquierda, clave)
				else:
					return __buscar(raiz.derecha, clave)
		
		aux = None
		if self.raiz is not None:
			aux = __buscar(self.raiz, clave)
		return aux
	
	def preorden(self):
		def __preorden(raiz):
			if raiz is not None:
				print(raiz.valor)
				__preorden(raiz.izquierda)
				__preorden(raiz.derecha)
		
		if self.raiz is not None:
			__preorden(self.raiz)
	
	def inorden(self):
		def __inorden(raiz):
			if raiz is not None:
				__inorden(raiz.izquierda)
				print(raiz.valor)
				__inorden(raiz.derecha)
		
		if self.raiz is not None:
			__inorden(self.raiz)
	
	def postorden(self):
		def __postorden(raiz):
			if raiz is not None:
				__postorden(raiz.derecha)
				print(raiz.valor)
				__postorden(raiz.izquierda)
		
		if self.raiz is not None:
			__postorden(self.raiz)
	
	def busqueda_de_proximidad(self, valor):
		def __buscar(raiz, valor):
			if raiz is not None:
				__buscar(raiz.izquierda, valor)
				if raiz.valor.startswith(valor):
					print(raiz.valor)
				__buscar(raiz.derecha, valor)
		
		if self.raiz is not None:
			__buscar(self.raiz, valor)
	
	def por_nivel(self):
		pendientes = Cola()
		if self.raiz is not None:
			pendientes.arribo(("--Raíz--", self.raiz, self.raiz.peso))
			nivel_aux = self.raiz.peso
		
		while pendientes.tamaño() > 0:
			direccion, nodo, nivel = pendientes.atencion()
			if nivel == nivel_aux:
				nivel_aux -= 1
				print(f"Nivel {nivel}:")
			print(f"   |{direccion}| {nodo.valor} (peso {nodo.peso}).")
			if nodo.izquierda is not None:
				pendientes.arribo((f"<--{nodo.valor}-- ", nodo.izquierda, nivel - 1))
			if nodo.derecha is not None:
				pendientes.arribo((f" --{nodo.valor}-->", nodo.derecha, nivel - 1))

	def eliminar_nodo(self, valor):
		def __reemplazar(raiz):
			if raiz.derecha is None:
				return raiz.izquierda, raiz
			else:
				raiz.derecha, nodo_reemplazado = __reemplazar(raiz.derecha)
				return raiz, nodo_reemplazado
		
		def __eliminar(raiz, valor):
			valor_borrado = None
			otro_valor_borrado = None
			if raiz is not None:
				if raiz.valor > valor:
					raiz.izquierda, valor_borrado, otro_valor_borrado = __eliminar(raiz.izquierda, valor)
				elif raiz.valor < valor:
					raiz.derecha, valor_borrado, otro_valor_borrado = __eliminar(raiz.derecha, valor)
				else:
					valor_borrado = raiz.valor
					otro_valor_borrado = raiz.otro_valor
					if raiz.izquierda is None:
						return raiz.derecha, valor_borrado, otro_valor_borrado
					elif raiz.derecha is None:
						return raiz.izquierda, valor_borrado, otro_valor_borrado
					else:
						raiz.izquierda, nodo_reemplazado = __reemplazar(raiz.izquierda)
						raiz.valor = nodo_reemplazado.valor
						raiz.otro_valor = nodo_reemplazado.otro_valor
					raiz = self.balanceo(raiz)
					self.actualizar_peso(raiz)
			return raiz, valor_borrado, otro_valor_borrado

		valor_borrado = None
		otro_valor_borrado = None
		if self.raiz is not None:
			self.raiz, valor_borrado, otro_valor_borrado = __eliminar(self.raiz, valor)
		return valor_borrado, otro_valor_borrado
	


	# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
	# A. Los índices de cada uno de los árboles deben ser nombre, número y tipo;
	def insertar_por_nombre(self, nombre, pokemon):
		self.insertar_nodo(nombre, pokemon)

	def insertar_por_numero(self, numero, pokemon):
		self.insertar_nodo(numero, pokemon)

	def insertar_por_tipo(self, tipo, pokemon):
		nodo = self.busqueda(tipo)
		if nodo:
			nodo.otro_valor.append(pokemon)
		else:
			self.insertar_nodo(tipo, [pokemon])

	# B. Mostrar todos los datos de un Pokémon a partir de su número y nombre -para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;

	def buscar_por_numero(self, numero):
		nodo = self.busqueda(numero)
		return nodo.otro_valor if nodo else None


	def buscar_por_nombre_aproximado(self, subcadena):
		resultados = []

		def __buscar_aprox(raiz):
			if raiz is not None:
				__buscar_aprox(raiz.izquierda)
				if subcadena.lower() in raiz.valor.lower():
					resultados.append(raiz.otro_valor)
				__buscar_aprox(raiz.derecha)

		__buscar_aprox(self.raiz)
		return resultados

	# C. Mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
	def listar_por_tipo(self, tipo):
		nodo = self.busqueda(tipo)
		return nodo.otro_valor if nodo else []

	# D. Realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
	def listar_ascendente(self):
		resultados = []

		def __inorden(raiz):
			if raiz is not None:
				__inorden(raiz.izquierda)
				resultados.append(raiz.otro_valor)
				__inorden(raiz.derecha)

		__inorden(self.raiz)
		return resultados

	# E. Mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
	def listar_por_nivel(self):
		if not self.raiz:
			return []
	
		pendientes = Cola()
		pendientes.arribo(self.raiz)
		resultados = []

		while pendientes.tamaño() > 0:
			nodo = pendientes.atencion()
			resultados.append(nodo.otro_valor)
			if nodo.izquierda:
				pendientes.arribo(nodo.izquierda)
			if nodo.derecha:
				pendientes.arribo(nodo.derecha)

		return resultados

	# F. Determina cuantos Pokémons hay de tipo eléctrico y acero.
	def contar_pokemons_por_tipo(self, tipo):
		nodo = self.busqueda(tipo)
		return len(nodo.otro_valor) if nodo else 0
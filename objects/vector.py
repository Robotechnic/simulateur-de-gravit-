class Vector:

	"""classe Vector
	implémentation du vecteur mathématique en python

	Attributes:
		x (float): coordonnée x du vecteur
		y (float): coordonnée y du vecteur
	"""

	def __init__(self, x=0.0, y=0.0):
		"""Summary

		Args:
			x (float, optional): coordonnée x du vecteur
			y (float, optional): coordonnée y du vecteur

		Raises:
			TypeError: les coordonnées doivent être des flotans
		"""
		try:
			self.x = float(x)
			self.y = float(y)
		except Exception as e:
			raise TypeError("x and y must be float numbers")

	def norme(self):
		"""calcule la norme du vecteur

		Returns:
			float: norme du vecteur
		"""
		return (self.x ** 2 + self.y ** 2) ** 0.5

	def __str__(self):
		"""converti le vecteur en chane de caractère

		Returns:
			string: le vecteur sous forme de string
		"""
		return "Vector : x=" + str(self.x) + " y=" + str(self.y)

	def __repr__(self):
		"""représentation du vecteur l'orsque l'on fait un print()
		ou qu'on l'affiche dans la console

		Returns:
			string: le vecteur sous forme de string (chaine de caractère)
		"""
		return self.__str__()

	def __add__(self, VectorObject):
		"""aplique l'opérateur + au vecteur avec un nombre ou un autre
		vecteur et retourne le nouveau vecteru créé

		Args:
			VectorObject (float ou Vecteur): vecteur ou nombre a ajouter

		Returns:
			Vector: résultat de l'adition des deux vecteur ou du vecteur et du nombre

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		temp = Vector()
		if type(VectorObject) == Vector:
			temp.x = self.x + VectorObject.x
			temp.y = self.y + VectorObject.y
		else:
			try:
				temp.x = self.x + float(VectorObject)
				temp.y = self.y + float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")
		return temp

	def __sub__(self, VectorObject):
		"""aplique l'opérateur - au vecteur avec un nombre ou un autre
		vecteur et retourne le nouveau vecteru créé

		Args:
			VectorObject (float ou Vecteur): vecteur ou nombre a soustraire

		Returns:
			Vector: résultat de la soustaction des deux vecteur ou du vecteur et du nombre

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		temp = Vector()
		if type(VectorObject) == Vector:
			temp.x = self.x - VectorObject.x
			temp.y = self.y - VectorObject.y
		else:
			try:
				temp.x = self.x - float(VectorObject)
				temp.y = self.y - float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")
		return temp

	def __mul__(self, VectorObject):
		"""aplique l'opérateur * au vecteur avec un nombre ou un autre
		vecteur et retourne le nouveau vecteru créé

		Args:
			VectorObject (float ou Vecteur): vecteur pour faire le produit scalaire ou nombre pour faire une multiplication

		Returns:
			Vector: résultat du produit scalaire des deux vecteur ou de la multiplication vecteur et du nombre

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		temp = Vector()
		if type(VectorObject) == Vector:
			temp.x = self.x * VectorObject.x
			temp.y = self.y * VectorObject.y
		else:
			try:
				temp.x = self.x * float(VectorObject)
				temp.y = self.y * float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")
		return temp

	def __truediv__(self, VectorObject):
		"""aplique l'opérateur / au vecteur avec un nombre ou un autre
		vecteur et retourne le nouveau vecteru créé

		Args:
			VectorObject (float ou Vecteur): vecteur ou nombre a diviser

		Returns:
			Vector: résultat de la division des deux vecteur ou du vecteur et du nombre

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		temp = Vector()
		if type(VectorObject) == Vector:
			temp.x = self.x / VectorObject.x
			temp.y = self.y / VectorObject.y
		else:
			try:
				temp.x = self.x / float(VectorObject)
				temp.y = self.y / float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")
		return temp

	def __iadd__(self, VectorObject):
		"""aplique l'opérateur += au vecteur

		Args:
			VectorObject (float ou vecteur): vecteur ou nombre a ajouter

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		if type(VectorObject) == Vector:
			self.x += VectorObject.x
			self.y += VectorObject.y
		else:
			try:
				self.x += float(VectorObject)
				self.y += float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")

	def __isub__(self, VectorObject):
		"""aplique l'opérateur -= au vecteur

		Args:
			VectorObject (float ou vecteur): vecteur ou nombre a soustraire

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		if type(VectorObject) == Vector:
			self.x -= VectorObject.x
			self.y -= VectorObject.y
		else:
			try:
				self.x -= float(VectorObject)
				self.y -= float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")

	def __imul__(self, VectorObject):
		"""aplique l'opérateur *= au vecteur

		Args:
			VectorObject (float ou vecteur): vecteur ou nombre pour faire un produit scalaire
			ou une multiplication

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		if type(VectorObject) == Vector:
			self.x *= VectorObject.x
			self.y *= VectorObject.y
		else:
			try:
				self.x *= float(VectorObject)
				self.y *= float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")

	def __itruediv__(self, VectorObject):
		"""aplique l'opérateur /= au vecteur

		Args:
			VectorObject (float ou vecteur): vecteur ou nombre a diviser

		Raises:
			TypeError: Si l'argument n'est pas un vecteur il doit être un nombre
		"""
		if type(VectorObject) == Vector:
			self.x /= VectorObject.x
			self.y /= VectorObject.y
		else:
			try:
				self.x /= float(VectorObject)
				self.y /= float(VectorObject)
			except Exception as e:
				raise TypeError("non Vector value must be float numbers")

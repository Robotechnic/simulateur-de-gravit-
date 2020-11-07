from modules.vector import *
from time import time

class Object:

	"""Class object qui ser de base a tous les corps celestes de la simulation
	les autres corps celeste héritent de cette classe pour simplifier le code final
	"""
	
	def __init__(self, x=0.0, y=0.0, mass=0.0, speed=Vector(), acceleration=Vector()):
		"""Constructeur de Object
		
		Args:
		    x (float, optional): position x de l'objet
		    y (float, optional): position y de l'objet
		    mass (float, optional): masse de l'objet
		    speed (Vector, optional): vitesse de l'objet
		    acceleration (Vector, optional): acceleration de l'objet
		
		Raises:
		    TypeError: retourne un erreur si les tyes des paramètres ne sont pas respectés
		"""
		self._id = -1
		try:
			self._x = float(x)
			self._y = float(y)
			self._mass = float(mass)
			
		except Exception as e:
			raise TypeError("x, y and mass must be float numbers")

		if not isinstance(acceleration, Vector):
			raise TypeError("acceleration is not a valid Vector")
		if not isinstance(speed, Vector):
			raise TypeError("speed vector is not a valid Vector")
		self._acceleration = acceleration
		self._speed = speed
		self._lastevolve = time()

	@property
	def x(self):
		"""renvoie x
		
		Returns:
		    float: x
		"""
		return self._x

	@x.setter
	def x(self, x):
		"""permet de vérifier la valeur de x avant modification
		
		Args:
		    x (float): la nouvelle valeur de x
		
		Raises:
		    TypeError: x doit être un nombre flotant
		"""
		try:
			self._x = x
		except Exception as e:
			raise TypeError("x must be a floating number")

	@property
	def y(self):
		"""renvoie y
		
		Returns:
		    float: y
		"""
		return self._y

	@y.setter
	def y(self, y):
		"""permet de vérifier la valeur de y avant modification
		
		Args:
		    y (float): la nouvelle valeur de y
		
		Raises:
		    TypeError: y doit être un nombre flotant
		"""
		try:
			self._y = y
		except Exception as e:
			raise TypeError("y must be a floating number")

	@property
	def mass(self):
		"""renvoie la masse de l'objet
		
		Returns:
		    float: mass
		"""
		return self._mass

	@mass.setter
	def mass(self, mass):
		"""permet de vérifier la valeur de mass avant modification
		
		Args:
		    mass (float): la nouvelle valeur de mass
		
		Raises:
		    TypeError: mass doit être un nombre flotant
		"""
		try:
			self._mass = mass
		except Exception as e:
			raise TypeError("mass must be a floating number")

	@property
	def id(self):
		"""renvoie id
		
		Returns:
		    int: id
		"""
		return self._id

	@id.setter
	def id(self, newId):
		"""permet de vérifier la valeur de id avant modification
		
		Args:
		    newId (int): la nouvelle valeur de id
		
		Raises:
		    TypeError: id doit être un nombre flotant
		"""
		try:
			self._id = int(newId)
		except Exception as e:
			raise TypeError("id must be an int")
	@property
	def acceleration(self):
		"""renvoie l'accélération de l'objet
		
		Returns:
		    Vector: acceleration
		"""
		return self._acceleration

	@acceleration.setter
	def acceleration(self, acceleration):
		"""permet de vérifier la valeur de l'accélération avant modification
		
		Args:
		    acceleration (Vector): la nouvelle valeur de acceleration
		
		Raises:
		    TypeError: acceleration doit être un Vector
		"""
		if not isinstance(acceleration,Vector):
			raise TypeError("acceleration must be a vector")
		else:
			self._acceleration = acceleration

	@property
	def speed(self):
		"""renvoie la vitesse de l'objet
		
		Returns:
		    Vector: speed
		"""
		return self._speed

	@speed.setter
	def speed(self, speed):
		"""permet de vérifier la valeur de la vitesse avant modification
		
		Args:
		    speed (Vector): la nouvelle valeur de speed
		
		Raises:
		    TypeError: speed doit être un Vector
		"""
		if not isinstance(speed,Vector):
			raise TypeError("acceleration must be a vector")
		else:
			self._speed = speed

	@property
	def lastevolve(self):
		"""renvoie la dernière fois que l'objet a évolué
		
		Returns:
		    float: lastevolve
		"""
		return self._lastevolve

	@lastevolve.setter
	def lastevolve(self, lastevolve):
		"""permet de vérifier la valeur de lastevolve avant modification
		
		Args:
		    lastevolve (float): la nouvelle valeur de lastevolve
		
		Raises:
		    TypeError: lastevolve doit être un nombre flotant
		"""
		try:
			self._lastevolve = int(lastevolve)
		except Exception as e:
			raise TypeError("lastevolve must be an integer")

	def __str__(self):
		"""représentation de l'objet sous forme de chaine de caractère
		
		Returns:
		    string: l'objet sous forme de string
		"""
		return (
			"Object : mass="
			+ str(self._mass)
			+ " x="
			+ str(self._x)
			+ " y="
			+ str(self._y)
			+ " speed="
			+ str(self._speed)
			+ " acceleration="
			+ str(self._acceleration)
		)

	def __repr__(self):
		"""représentation de l'objet lorsqu'on l'affiche dans la console
		
		Returns:
		    string: la représentation sous forme de chaine de caractères l'objet
		"""
		return self.__str__()

	@staticmethod
	def gravitationStrenght(ma, mb, d):
		"""calcule la force d'atraction gravitationelle entre deux objets
		
		Args:
		    ma (float): masse de l'objet a
		    mb (float): masse de l'objet b
		    d (float): distance entre les deux objets
		
		Returns:
		    float: la force d'atraction gravitationelle
		"""
		return float(6.67408e-11*(ma*mb)/(pow(d,2)))

	@staticmethod
	def getDistance(objecta, objectb):
		"""calcule la distance entre deux objets
		
		Args:
		    objecta (Object): objet a
		    objectb (Object): objet b
		
		Returns:
		    float: la distance entre les deux objets
		
		Raises:
		    TypeError: Les deux objets doivent êtres de type Object ou hériter de Object
		"""
		if not isinstance(objecta, Object) or not isinstance(objectb, Object):
			raise TypeError("Please provide two valid objects")

		return ((objectb.x - objecta.x) ** 2 + (objectb.y - objecta.y) ** 2) ** 0.5

	def getDistance(self, objectb):
		"""retourne la distance entre l'objet actuel et un autre objet
		
		Args:
		    objectb (Object): l'objet b
		
		Returns:
		    float: la distance entre l'objet actuel et l'autre objet
		
		Raises:
		    TypeError: Il faut que l'objet b soit de type Object ou qu'il hérite de Object
		"""
		if not isinstance(objectb, Object):
			raise TypeError("Please provide a valid object")

		return ((objectb.x - self._x) ** 2 + (objectb.y - self._y) ** 2) ** 0.5

	@staticmethod
	def getGravitationStrenght(objecta, objectb):
		"""calcule la force d'atraction gravitationelle de b sur a
		
		Args:
		    objecta (Object): objet a
		    objectb (Object): objet b
		
		Returns:
		    Vector: la force d'atraction gravitationelle de b sur a
		
		Raises:
		    TypeError: les object en paramètre doivent être de type Object ou hériter de Object
		"""
		if not isinstance(objecta, Object) or not isinstance(objectb, Object):
			raise TypeError("Please provide two valid objects")

		distance = Object.getDistance(objecta, objectb)
		strenght = Object.gravitationStrenght(objecta.mass, objectb.mass, distance)

		return Vector(
			(objectb.x - objecta.x) / distance * strenght + objecta.x,
			(objectb.y - objecta.y) / distance * strenght + objecta.y,
		)

	def getGravitationStrenght(self, objectb):
		"""calcule la force d'atracton gravitationelle de b sur l'objet actuel
		
		Args:
		    objectb (Object): autre objet a étudier
		
		Returns:
		    Vector: le vecteur d'atraction gravitationelle de b sur l'objet actuel
		
		Raises:
		    TypeError: l'objet en paramètre doit être un objet ou hériter de Object
		"""
		if not isinstance(objectb, Object):
			raise TypeError("Please provide a valid object")

		distance = self.getDistance(objectb)
		strenght = Object.gravitationStrenght(self._mass, objectb.mass, distance)

		return Vector(
			(objectb.x - self._x) / distance * strenght + self._x,
			(objectb.y - self._y) / distance * strenght + self._y,
		)

	def applyStrenght(self,other):
		"""calcule l'accélération de l'objet a partir des forces et des autres objects passé en paramètre
		
		Args:
		    other: liste des objects ou des forces a apliquer
		
		Raises:
		    TypeError: other doit contenir uniquement des Vector, des Object ou des objects qui hérient de Object ou de Vector
		"""

		fSumm = Vector()
		for obj in other:
			if isinstance(obj, Object):
				if obj.id != self._id and obj.id != -1:
					fSumm += self.getGravitationStrenght(obj)
			elif isinstance(obj, Vector):
				fSumm += obj
			else:
				raise TypeError("Please provide a Vector or an Object")
		self._acceleration= fSumm / self._mass

		print(self._id,self._acceleration,fSumm)

	def evolve(self):
		"""fait évoluer l'objet en calculans la nouvelle vitesse et en l'apliquant au coordonnées
		"""
		last = time() - self._lastevolve
		self._lastevolve= time()

		self._speed += self._acceleration* last
		
		self._x += self._speed.x * last
		self._y += self._speed.y * last

	def draw():
		"""dessine l'objet pas possible ici puisuqe objet est juste une classe de calcul
		par contre, c'est obligatoire si on hérite de Object
		
		Raises:
		    NotImplemented: Cette fonction doit être inplémenté dans les enfants de la classe Object
		"""
		raise NotImplemented()

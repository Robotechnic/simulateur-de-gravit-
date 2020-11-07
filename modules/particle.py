"""Summary
"""
from modules.objects import *
from tkinter import Canvas

class Particle(Object):

	"""Summary
	"""
	
	def __init__(self,x=0.0,y=0.0,mass=0.0,radius=0.0,speed=Vector(),acceleration=Vector()):
		"""Summary
		
		Args:
		    x (float, optional): Description
		    y (float, optional): Description
		    mass (float, optional): Description
		    radius (float, optional): Description
		    speed (TYPE, optional): Description
		    acceleration (TYPE, optional): Description
		
		Raises:
		    TypeError: Description
		"""
		Object.__init__(self,x,y,mass,speed,acceleration)
		try:
			self._radius = float(radius)
		except Exception as e:
			raise TypeError("radius mus be a float value")

	@property
	def radius(self):
		"""renvoie radius
		
		Returns:
		    float: radius
		"""
		return self._radius

	@radius.setter
	def radius(self, radius):
		"""permet de vérifier la valeur du rayon avant modification
		
		Args:
		    radius (float): la nouvelle valeur de radius
		
		Raises:
		    TypeError: radius doit être un nombre flotant
		"""
		try:
			self._radius = radius
		except Exception as e:
			raise TypeError("radius must be an floating number")

	def __str__(self):
		"""représentation de l'objet sous forme de chaine de caractère
		
		Returns:
		    string: l'objet sous forme de string
		"""
		return (
			"Particle : mass="
			+ str(self._mass)
			+ " radius="
			+ str(self._radius)
			+ " x="
			+ str(self._x)
			+ " y="
			+ str(self._y)
			+ " speed="
			+ str(self._speed)
			+ " acceleration="
			+ str(self._acceleration)
		)

	def draw(self,canvas):
		"""dessine l'objet a l'écran
		
		Args:
		    canvas (tkinter.Canvas): zone de dessin
		"""
		if self._id == -1:
			self._id = canvas.create_oval(self._x,self._y,self._x+self._radius,self._y+self._radius,fill="white")
		else:
			canvas.coords(self._id,self._x,self._y,self._x+self._radius,self._y+self._radius)
from tkinter import Canvas
from modules.vector import *
from modules.objects import *
from modules.particle import *


class Space(Canvas):
	def __init__(self, parent, **kwargs):
		Canvas.__init__(self, parent, **kwargs)
		self.spaceObjects = list()

	def addParticle(self, x, y, mass, radius):
		self.spaceObjects += [Particle(x, y, mass, radius)]
		self.spaceObjects[len(self.spaceObjects) - 1].draw(self)

	def update(self):
		for obj in self.spaceObjects:
			obj.applyStrenght(self.spaceObjects)
			obj.evolve()
			obj.draw(self)

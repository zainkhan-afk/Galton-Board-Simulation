from vector import Vector
import random
from settings import *

class Particle:
	def __init__(self, x = None, y = None, mass = 1, radius = 10, color = None):
		if x is None or y is None:
			self.pos = Vector(x = random.randint(0, WIDTH), y = random.randint(0, HEIGHT))
		else:
			self.pos = Vector(x = x, y = y)
		self.vel = Vector(x = random.randint(-2, 2), y = 0)
		self.vel = Vector(x = 3, y = 0)
		self.acc = Vector(x = 0, y = 0)
		self.mass = mass
		self.radius = radius
		self.tail = [[int(self.pos.x), int(self.pos.y)]]

		if color is None:
			self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
		else:
			self.color = color


	def update(self, acc):
		self.acc = acc
		self.vel += self.acc*DELTA_T
		self.pos += self.vel*DELTA_T

		self.tail.append([int(self.pos.x), int(self.pos.y)])
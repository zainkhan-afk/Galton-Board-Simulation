import numpy as np
from vector import Vector
from settings import *

class Physics:
	def __init__(self):
		self.g = Vector(x = 0.0, y = 9)

	def check_collisions(self, particles):
		collision_pairs = []
		for p1 in particles:
			for p2 in particles:
				if p1 == p2 or [p1, p2] in collision_pairs:
					continue
				direction = p1.pos - p2.pos 
				R = direction.magnitude
				if R<=(p1.radius + p2.radius):
					collision_pairs.append([p1, p2])
					collision_pairs.append([p2, p1])

					vel_diff = p1.vel - p2.vel

					e = 1
					j = -(1+e)*vel_diff.dot(vel_diff.normalize())
					j = j / (1/p1.mass + 1/p2.mass)

					# print(vel_diff.normalize())
					# print(p1.vel)

					p1.vel = p1.vel + vel_diff.normalize() * (j/p1.mass)
					p2.vel = p2.vel - vel_diff.normalize() * (j/p2.mass)

					# while R<=(p1.radius + p2.radius):
					# 	p1.update(Vector(x = 0, y = 0))
					# 	p2.update(Vector(x = 0, y = 0))
					# 	direction = p1.pos - p2.pos 
					# 	R = direction.magnitude

			p1.update(self.g)


	def update(self, particles):
		for p in particles:
			if p.pos.y + p.radius > HEIGHT:
				p.vel.y *= -1
				p.pos.y = HEIGHT - p.radius

			if p.pos.x + p.radius > WIDTH:
				p.vel.x *= -1
				p.pos.x = WIDTH - p.radius

			elif p.pos.x + p.radius < 0:
				p.vel.x *= -1
				p.pos.x = 0

			p.update(self.g)
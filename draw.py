import numpy as np
import cv2

class Draw:
	def __init__(self, width, height):
		self.height = height
		self.width = width

		self.clear_canvas()

	def clear_canvas(self):
		self.canvas = np.zeros((self.height, self.width, 3)).astype("uint8")

	def get_particle_mask(self, particle, particle_mask):
		x = int(particle.pos.x)
		y = int(particle.pos.y)

		cv2.circle(particle_mask, (x, y), particle.radius, (255, 255, 255), -1)

		return particle_mask

	def get_particle_tail(self, particle, particle_tail_mask):
		x = int(particle.pos.x)
		y = int(particle.pos.y)

		cv2.polylines(particle_tail_mask, [np.array(particle.tail)], False, 255, 1)

		return particle_tail_mask

	def draw(self, particles, borders):
		for particle in particles:
			x = int(particle.pos.x)
			y = int(particle.pos.y)

			cv2.circle(self.canvas, (x, y), particle.radius+2, particle.color, -1)


		self.canvas = cv2.GaussianBlur(self.canvas,(17,17),0)
		for border in borders:
			cv2.line(self.canvas, (border.x1, border.y1), 
						(border.x2, border.y2), border.color, border.thickness)

		for particle in particles:
			x = int(particle.pos.x)
			y = int(particle.pos.y)

			cv2.circle(self.canvas, (x, y), particle.radius, particle.color, 1)


	def render(self):
		cv2.imshow("canvas", self.canvas)
		return cv2.waitKey(30)

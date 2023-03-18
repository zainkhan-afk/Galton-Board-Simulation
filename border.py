import numpy as np

class Border:
	def __init__(self, x1, y1, x2, y2, color = (125, 125, 125), thickness = 3):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

		self.color = color
		self.thickness = thickness
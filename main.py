from draw import Draw
from particle import Particle
from border import Border
from physics import Physics
from settings import *

canvas = Draw(WIDTH, HEIGHT)
physics_engine = Physics()

borders = []
balls = [Particle() for i in range(NUM_PARTICLES)]


borders.append(Border(x1 = 0, y1 = HEIGHT//3, x2 = WIDTH//2 - 10, y2 = 0))
borders.append(Border(x1 = WIDTH//2 + 10, y1 = 0, x2 = WIDTH, y2 = HEIGHT//3))

div = WIDTH//NUM_BINS
for i in range(NUM_BINS + 1):
	b = Border(x1 = i*div, y1 = HEIGHT//2, x2 = i*div, y2 = HEIGHT)
	borders.append(b)

board_p = []
board_pts_y_start = 150
horizaontal_dist = 35
vertical_dist = 60

# for i in range(5):
# 	for j in range(-i, i+1):
# 		p = Particle(x = WIDTH//2 + j*horizaontal_dist, 
# 			y = board_pts_y_start + i*vertical_dist, 
# 			radius = 3, color = (255, 255, 255))
# 		board_p.append(p)

# 		p = Particle(x = (WIDTH//2 - horizaontal_dist//2) + j*horizaontal_dist, 
# 			y = (board_pts_y_start + vertical_dist//2) + i*vertical_dist, 
# 			radius = 3, color = (255, 255, 255))
# 		board_p.append(p)
# 	p = Particle(x = (WIDTH//2 - horizaontal_dist//2) + (i+1)*horizaontal_dist, 
# 		y = (board_pts_y_start + vertical_dist//2) + i*vertical_dist, radius = 3, 
# 		color = (255, 255, 255))
# 	board_p.append(p)

while True:
	physics_engine.check_collisions(balls)

	canvas.clear_canvas()
	canvas.draw(balls, borders)
	# canvas.draw(board_p)
	k = canvas.render()

	if k == ord("q"):
		break
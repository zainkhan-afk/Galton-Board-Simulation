from draw import Draw
from particle import Particle
from physics import Physics
from settings import *

canvas = Draw(WIDTH, HEIGHT)
physics_engine = Physics()

balls = [Particle() for i in range(NUM_PARTICLES)]


balls = []


balls.append(Particle(x = WIDTH//2, y = HEIGHT -250))
balls.append(Particle(x = WIDTH//2, y = HEIGHT -200))
balls.append(Particle(x = WIDTH//2, y = HEIGHT -150))
balls.append(Particle(x = WIDTH//2, y = HEIGHT -100))
balls.append(Particle(x = WIDTH//2, y = HEIGHT - 50))

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
	canvas.draw(balls)
	# canvas.draw(board_p)
	k = canvas.render()

	if k == ord("q"):
		break
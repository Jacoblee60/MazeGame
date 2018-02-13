import random
from scene import *
import ui
import time

class MyScene (Scene):
	def setup(self):
		width = 10
		height = width*2
		self.maze, end_x, end_y, path = genMaze(width, height)
		self.div_h = self.size.h/(height+2)
		self.div_w = self.size.w/(width+2)
		div_h = self.div_h
		div_w = self.div_w
		self.background_color = '#dfebc6'
		
		drawSeg(self, 'red', div_w*(end_x+1), div_h*(end_y+1), div_w, div_h)
		drawSeg(self, 'green', div_w, div_h, div_w, div_h)
		drawSeg(self, 'black', div_w*(width+1), div_h, 1, div_h*height)
		drawSeg(self, 'black', div_w, div_h*(height+1), div_w*width, 1)
					
		for x in range(0, width):
			for y in range(0, height):
				if self.maze[y][x] in [1,11]:
					drawSeg(self, 'black', div_w*(x+1), div_h*(y+1), 1, div_h)
				if self.maze[y][x] in [10,11]:
					drawSeg(self, 'black', div_w*(x+1), div_h*(y+1), div_w, 1)
					
		self.ball = ShapeNode(ui.Path.oval(0,0,2*div_w/3,2*div_h/3), 'gray', 'gray', shadow=None)
		self.ball.anchor_point = (0.5,0.5)
		self.moving = False
		self.x = 0
		self.y = 0
		self.ball.position = div_w*1.5,div_h*1.5
		self.add_child(self.ball)
		
	def touch_began(self, touch):
		self.touch_start = touch.location
		
	def touch_ended(self, touch):
		if self.moving:
			return
		self.touch_end = touch.location
		dy = self.touch_end.y - self.touch_start.y
		dx = self.touch_end.x - self.touch_start.x
		up = dy > 0
		down = dy < 0
		left = dx < 0
		right = dx > 0
		if right and (abs(dx)>abs(dy)) and not(self.maze[self.y][self.x+1] in [1,11]):
			a = [Action.move_by(self.div_w,0,.15), Action.call(self.endMove)]
			self.x = self.x+1
		elif left and (abs(dx)>abs(dy)) and not(self.maze[self.y][self.x] in [1,11]):
			a = [Action.move_by(-self.div_w,0,.15), Action.call(self.endMove)]
			self.x -= 1
		elif up and (abs(dx)<abs(dy)) and not(self.maze[self.y+1][self.x] in [10,11]):
			a = [Action.move_by(0,self.div_h,.15), Action.call(self.endMove)]
			self.y += 1
		elif down and (abs(dx)<abs(dy)) and not(self.maze[self.y][self.x] in [10,11]):
			a = [Action.move_by(0,-self.div_h,.15), Action.call(self.endMove)]
			self.y -= 1
		else:
			a = [Action.call(self.endMove)]
			
		self.moving = True
		self.ball.run_action(Action.sequence(a))

	def endMove(self):
		self.moving = False

def drawSeg(self, color, x, y, width, height):
	seg = ui.Path.rect(0,0,width,height)
	self.segment = ShapeNode(seg, color, color, shadow=None)
	self.segment.anchor_point = (0,0)
	self.segment.position = (x,y)
	self.add_child(self.segment)
		
def genMaze(width, height):
		path = 0
		x = 0
		y = 0
		directions = ["N","E","S","W"]
		coord_stack = []
		exist_set = {}
		maze = []
		begin = True
		for i in range(0,height):
			row = []
			for j in range(0,width):
				row.append(11)
			maze.append(row)
			
		end = False
		
		while (begin == True) or ((x,y) != (0,0)):
			begin = False
			exist_set[(x,y)]=True
			random.shuffle(directions)
			valid = False
			i = 0
			
			while valid != True:
				a = (directions[i] == "N") and (y+1 < height) and not((x,y+1) in exist_set)
				b = (directions[i] == "E") and (x+1 < width) and not((x+1,y) in exist_set)
				c = (directions[i] == "S") and (y-1 >= 0) and not((x,y-1) in exist_set)
				d = (directions[i] == "W") and (x-1 >= 0) and not((x-1,y) in exist_set)
				
				if len(coord_stack) > path:
						path = len(coord_stack)
						end_x = x
						end_y = y
				if a or b or c or d:
					valid = True
					coord_stack.append((x,y))
				elif not(a or b or c or d) and i == 3:
					x,y = coord_stack.pop()
					break
				else:
					i += 1

			if valid == True:
				if directions[i] == "N":
					maze[y+1][x] -= 10
					y += 1
				if directions[i] == "E":
					maze[y][x+1] -= 1
					x += 1
				if directions[i] == "S":
					maze[y][x] -= 10
					y -= 1
				if directions[i] == "W":
					maze[y][x] -= 1
					x -= 1
		return maze, end_x, end_y, path
	
run(MyScene(), multi_touch=False)
			
	


	
	
	
	

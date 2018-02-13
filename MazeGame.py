import random
from scene import *
import ui

class MyScene (Scene):
	def setup(self):
		width = 10
		height = 20
		maze = genMaze(width, height)
		div_h = self.size.h/(height+2)
		div_w = self.size.w/(width+2)
		self.background_color = '#dfebc6'

		drawSeg(self, div_w*(width+1), div_h, 1, div_h*height)
		drawSeg(self, div_w, div_h*(height+1), div_w*width, 1)
					
		for x in range(0, width):
			for y in range(0, height):
				if maze[y][x] in [1,11]:
					drawSeg(self, div_w*(x+1), div_h*(y+1), 1, div_h)
				if maze[y][x] in [10,11]:
					drawSeg(self, div_w*(x+1), div_h*(y+1), div_w, 1)

def drawSeg(self, x, y, width, height):
	seg = ui.Path.rect(0,0,width,height)
	self.segment = ShapeNode(seg, '#000000', '#000000', shadow=None)
	self.segment.anchor_point = (0,0)
	self.segment.position = (x,y)
	self.add_child(self.segment)
		
def genMaze(width, height):
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
		return maze
	
run(MyScene())
			
	


	
	
	
	

import random

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

width = 20
height = 20

maze = genMaze(width,height)
top = ""
for i in range(0, width):
	top += " _"
print(top)
for i in reversed(maze):
	row = ""
	for j in i:
		if j == 0:
			row += "  "
		if j == 1:
			row += "| "
		if j == 10:
			row += " _"
		if j == 11:
			row += "|_"
	print(row+"|")
		

				
			
	


	
	
	
	

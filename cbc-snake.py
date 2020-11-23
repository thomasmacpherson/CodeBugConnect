# Written by Tom Macpherson-Pope
# https://github.com/thomasmacpherson/CodeBugConnect/cbc-snake.py
import time
import cbc
import random
snakeColour = cbc.Color('#002200')
appleColour = cbc.Color('#330000')
snakeHeadColour = cbc.Color('#222200')
black = cbc.Color('#000000')

north = [1,0] # x=0 y=+1
south = [-1,0] # x=0 y=-1
east = [0,-1] # x=-1 y=0
west = [0,1] # x=+1 y=0

delay = .5

y = 0
x = 1

while True:
	cbc.display.clear()
	game = True
	score = 0
	snake = [[1,2],[2,2]]
	heading = north
	newApple = True

	while game:
		if newApple:
			score = score + 1
			newApple = False
			while True:
				print("Creating apple")
				newAppleY = random.randint(0,4)
				newAppleX = random.randint(0,4)
				if cbc.display.get(newAppleX, newAppleY) != snakeColour and cbc.display.get(newAppleX, newAppleY) != snakeHeadColour :
					cbc.display.pixels[newAppleY, newAppleX] = appleColour
					print("Apple created")
					break

		if cbc.joystick_b.right_pressed and (heading != east):
			heading = west
		elif cbc.joystick_b.left_pressed and (heading != west):
			heading = east
		elif cbc.joystick_b.down_pressed and (heading != south):
			heading = north
		elif cbc.joystick_b.up_pressed and (heading != north):
			heading = south

		newX = (snake[-1][x] + heading[x]) % 5
		newY = (snake[-1][y] + heading[y]) % 5

		if cbc.display.get(newX, newY) != appleColour:
			cbc.display.pixels[snake[0][y], snake[0][x]] = black	
			del(snake[0])
		else:
			newApple = True
			print("Apple eaten")

		if  cbc.display.get(newX,newY) == snakeColour:
			game = False
		else:
			cbc.display.pixels[snake[-1][y],snake[-1][x]] = snakeColour
			snake.append([newY, newX])
			cbc.display.pixels[newY, newX] = snakeHeadColour

		time.sleep(delay)
		if not game:
			cbc.display.scroll_text('GAME OVER', fg=cbc.Color('#000080'))
			cbc.display.scroll_text('SCORE:', fg=cbc.Color('#00ff00'))
			cbc.display.scroll_text(str(score), fg=cbc.Color('#ff0080'))
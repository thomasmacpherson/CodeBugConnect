 # Written by Tom Macpherson-Pope
# https://github.com/thomasmacpherson/CodeBugConnect/cbc-frogger.py
import time
import cbc
cbc.display.clear()

playerX = 0
playerY = 0
playerColour = cbc.Color("green")
carColour = cbc.Color("red")
truckColour = cbc.Color("purple")
bikeColour = cbc.Color("yellow")
logColour = cbc.Color("brown")
waterColour = cbc.Color("blue")
playerMovementDelay = .2


while True:
	change= True
	game = True
	score = 0
   
	bikeX = 2
	bike2X = 4
	bikeY = 1
	
	carX = 0
	car2X = 3
	carY = 2

	truckY= 3
	truckX = 3
	truckX2 = 4
	
	waterY = 4
	waterX = 2
	waterX2 = 4

	speed = 20

	carMovementDelay = 4 * speed
	carMovementCount = carMovementDelay
	
	truckMovementDelay = 2 * speed
	truckMovementCount = truckMovementDelay
	
	bikeMovementDelay = 4 * speed
	bikeMovementCount = bikeMovementDelay
	
	waterMovementDelay = 4 *speed
	waterMovementCount = waterMovementDelay
	
	
	
	while game:
		#time.sleep(playerMovementDelay)
		if cbc.joystick_a.left_pressed and playerX > 0:
			#cbc.display.pixels[playerY, playerX] = cbc.Color("black")
			playerX = playerX -1
			change= True
			time.sleep(playerMovementDelay)
		elif cbc.joystick_a.right_pressed and playerX < 4:
			#cbc.display.pixels[playerY, playerX] = cbc.Color("black")
			playerX = playerX +1
			change= True
			time.sleep(playerMovementDelay)

		elif cbc.joystick_a.up_pressed:
			time.sleep(playerMovementDelay)
			bikeY =  (bikeY + 1) %5
			carY = (carY + 1) %5
			truckY = (truckY + 1) %5
			waterY =  (waterY + 1) %5
			score = score - 1
			change= True

			
		elif cbc.joystick_a.down_pressed:
			time.sleep(playerMovementDelay)
			bikeY = (bikeY - 1) %5
			carY = (carY - 1) %5
			truckY = (truckY - 1) %5
			waterY = (waterY - 1) %5
			score = score + 1
			change= True


		if bikeMovementCount == 0:
			bikeX = (bikeX - 1) %5
			bike2X = (bike2X - 1) %5       
			bikeMovementCount = bikeMovementDelay
			change= True

			#print("Car X move")
		else:
			bikeMovementCount = bikeMovementCount -1
			#print(carMovementCount)
			
			
		if carMovementCount == 0:
			carX = (carX + 1) %5
			car2X = (car2X + 1) %5       
			carMovementCount = carMovementDelay
			change= True

			#print("Car X move")
		else:
			carMovementCount = carMovementCount -1
			#print(carMovementCount)

		if truckMovementCount == 0:
			truckX = (truckX - 1) %5
			truckX2 = (truckX2 - 1) %5       
			truckMovementCount = truckMovementDelay
			change= True

			#print("Car X move")
		else:
			truckMovementCount = truckMovementCount -1
			#print(carMovementCount)

			
		if waterMovementCount == 0:
			waterX = (waterX + 1) %5
			waterX2 = (waterX2 + 1) %5  
			waterMovementCount = waterMovementDelay
			change= True

			#print("Car X move")
		else:
			waterMovementCount = waterMovementCount -1
			#print(carMovementCount)            
			
		if change:	
			cbc.display.clear()
			cbc.display.pixels[bikeY, bikeX] = bikeColour
			cbc.display.pixels[bikeY, bike2X] = bikeColour
			cbc.display.pixels[carY, carX] = carColour
			cbc.display.pixels[carY, car2X] = carColour
			cbc.display.pixels[truckY, truckX] = truckColour
			cbc.display.pixels[truckY, truckX2] = truckColour
			cbc.display.pixels[waterY, (waterX+1)%5] = logColour
			cbc.display.pixels[waterY, (waterX2+1)%5] = logColour
			cbc.display.pixels[waterY, (waterX2+2)%5] = logColour		
			cbc.display.pixels[waterY, waterX] = waterColour
			cbc.display.pixels[waterY, waterX2] = waterColour
			cbc.display.pixels[playerY, playerX] = playerColour
			change= False



		if (playerX == waterX and playerY == waterY) or (playerX == waterX2 and playerY == waterY) or (playerX == bikeX and playerY == bikeY) or (playerX == bikeX and playerY == bikeY) or (playerX == bike2X and playerY == bikeY) or (playerX == carX and playerY == carY) or (playerX == car2X and playerY == carY) or (playerX == truckX and playerY == truckY) or (playerX == truckX2 and playerY == truckY):
			game = False
			cbc.display.scroll_text('GAME OVER', fg=cbc.Color('#000080'))
			cbc.display.scroll_text('SCORE:', fg=cbc.Color('#00ff00'))
			cbc.display.scroll_text(str(score), fg=cbc.Color('#ff0080'))

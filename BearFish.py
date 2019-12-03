import turtle
from random import *
import datetime
import csv
class World(object):
	def __init__(self,mx,my):
		self.maxX = mx
		self.maxY = my
		self.thingList = []
		self.grid = []

		for arow in range(self.maxY):
			row = []
			for acol in range(self.maxX):
				row.append(None)
			self.grid.append(row)

		self.wturtle = turtle.Turtle()
		self.wscreen = turtle.Screen()
		self.wscreen.setworldcoordinates(0,0,self.maxX - 1,self.maxY - 1)
		#self.wscreen.addshape("Bear.gif")
		#self.wscreen.addshape("Fish.gif")
		self.wturtle.hideturtle()

	def draw(self):
		self.wscreen.tracer(0)
		self.wturtle.forward(self.maxX - 1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxY - 1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxX - 1)
		self.wturtle.left(90)
		self.wturtle.forward(self.maxY - 1)
		self.wturtle.left(90)
		for i in range(self.maxY -1):
			self.wturtle.forward(self.maxX - 1)
			self.wturtle.backward(self.maxX - 1)
			self.wturtle.left(90)
			self.wturtle.forward(1)
			self.wturtle.right(90)
		self.wturtle.forward(1)
		self.wturtle.right(90)
		for i in range(self.maxX - 2):
			self.wturtle.forward(self.maxY - 1)
			self.wturtle.backward(self.maxY - 1)
			self.wturtle.left(90)
			self.wturtle.forward(1)
			self.wturtle.right(90)
		self.wscreen.tracer(1)

	def freezeWorld(self):
		self.wscreen.exitonclick()

	def addThing(self, athing, x, y,tickCounter,starveCounter):
		athing.setX(x)
		athing.setY(y)
		athing.breedTickCounter = tickCounter
		self.grid[y][x] = athing
		athing.setWorld(self)
		self.thingList.append(athing)
		athing.appear(x,y)
		if isinstance(athing,Bear):
			athing.starveTickCounter = starveCounter

	def delThing(self, athing):
		athing.hide()
		self.grid[athing.getY()][athing.getX()] = None
		if athing in self.thingList:
			self.thingList.remove(athing)

	def moveThing(self,oldx,oldy,newx,newy):
		self.grid[newy][newx] = self.grid[oldy][oldx]
		self.grid[oldy][oldx] = None

	def getMaxX(self):
		return self.maxX

	def getMaxY(self):
		return self.maxY

	def liveALittle(self):
		if self.thingList != [] :
			athing = randrange(len(self.thingList))
			randomthing = self.thingList[athing]
			randomthing.liveALittle()

	def emptyLocation(self, x, y):
		if self.grid[y][x] == None:
			return True
		else:
			return False

	def lookAtLocation(self,x,y):
		return self.grid[y][x]

class Fish(object):

	def __init__(self):
		self.turtle = turtle.Turtle()
		self.turtle.up()
		self.turtle.hideturtle()
		self.turtle.color("red","red")
		self.turtle.shape("circle")

		self.xpos = 0
		self.ypos = 0
		self.world = None

		self.breedTick = 0
		self.breedTickCounter = 0

	def setX(self,newx):
		self.xpos = newx

	def setY(self,newy):
		self.ypos = newy

	def getX(self):
		return self.xpos

	def getY(self):
		return self.ypos

	def setWorld(self,aworld):
		self.world = aworld

	def appear(self,x,y):
		self.setX(x)
		self.setY(y)
		self.turtle.setposition(self.getX(),self.getY())
		self.turtle.showturtle()

	def hide(self):
		self.turtle.hideturtle()

	def move(self,newx,newy):
		self.world.moveThing(self.getX(),self.getY(),newx,newy)
		self.setX(newx)
		self.setY(newy)
		self.turtle.setposition(self.getX(),self.getY())

	def liveALittle(self):
		offsetList = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

		adjfish = 0
		for offset in offsetList:
			newx = self.getX() + offset[0]
			newy = self.getY() + offset[1]
			if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
				if(not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Fish):
					adjfish = adjfish + 1

		if adjfish >= 2:
			self.world.delThing(self)
		else:
			self.breedTick = self.breedTick + 1
			if self.breedTick >= self.breedTickCounter:
				self.tryToBreed()
			self.tryToMove()

	def tryToBreed(self):
		newFish = Fish()
		x = randrange(self.world.getMaxX())
		y = randrange(self.world.getMaxY())
		while not self.world.emptyLocation(x,y):
			x = randrange(self.world.getMaxX())
			y = randrange(self.world.getMaxY())
		self.world.addThing(newFish, x, y, self.breedTickCounter,0)
		self.breedTick = 0

	def tryToMove(self):
		offsetList = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

		for offset in offsetList:
			newpos = randrange(len(offsetList))
			newxy = offsetList[newpos]
			newx = self.getX() + newxy[0]
			newy = self.getY() + newxy[1]
			if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
				if self.world.emptyLocation(newx,newy):
					self.move(newx,newy)
					break

class Bear(object):

	def __init__(self):
		self.turtle = turtle.Turtle()
		self.turtle.up()
		self.turtle.hideturtle()
		self.turtle.color("brown","brown")
		self.turtle.shape("square")

		self.xpos = 0
		self.ypos = 0
		self.world = None

		self.breedTick = 0
		self.breedTickCounter = 0

		self.starveTick = 0
		self.starveTickCounter = 0

	def setX(self,newx):
		self.xpos = newx

	def setY(self,newy):
		self.ypos = newy

	def getX(self):
		return self.xpos

	def getY(self):
		return self.ypos

	def setWorld(self,aworld):
		self.world = aworld

	def appear(self,x,y):
		self.setX(x)
		self.setY(y)
		self.turtle.setposition(self.getX(),self.getY())
		self.turtle.showturtle()

	def hide(self):
		self.turtle.hideturtle()

	def move(self,newx,newy):
		self.world.moveThing(self.getX(),self.getY(),newx,newy)
		self.setX(newx)
		self.setY(newy)
		self.turtle.setposition(self.getX(),self.getY())

	def liveALittle(self):
		offsetList = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

		adjbear = 0
		for offset in offsetList:
			newx = self.getX() + offset[0]
			newy = self.getY() + offset[1]
			if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
				if(not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Bear):
					adjbear = adjbear + 1
				if(not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx,newy),Fish):
					self.world.delThing(self.world.lookAtLocation(newx,newy))
					self.starveTick = 0
					break

		if adjbear >= 2:
			self.world.delThing(self)
		elif self.starveTick >= self.starveTickCounter:
				self.world.delThing(self)
		else:
			self.breedTick = self.breedTick + 1
			if self.breedTick >= self.breedTickCounter:
				self.tryToBreed()
			self.tryToMove()
			self.starveTick = self.starveTick + 1

	def tryToBreed(self):
		newBear = Bear()
		x = randrange(self.world.getMaxX())
		y = randrange(self.world.getMaxY())
		while not self.world.emptyLocation(x,y):
			x = randrange(self.world.getMaxX())
			y = randrange(self.world.getMaxY())
		self.world.addThing(newBear, x, y, self.breedTickCounter,self.starveTickCounter)
		self.breedTick = 0

	def tryToMove(self):
		offsetList = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

		for offset in offsetList:
			newpos = randrange(len(offsetList))
			newxy = offsetList[newpos]
			newx = self.getX() + newxy[0]
			newy = self.getY() + newxy[1]
			if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
				if self.world.emptyLocation(newx,newy):
					self.move(newx,newy)
					break

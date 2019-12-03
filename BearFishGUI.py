from tkinter import *
from tkinter import messagebox
from BearFish import *
import turtle

class BearFishGUI(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.turtleSpeed = 6
		self.fishBreedTick = 0
		self.bearBreedTick = 0
		self.bearStarveTick = 0

		self.master.title("Bear V.S. Fish")
		self.grid()

		# Number of Fish
		self.FishLabel = Label(self, text="Enter the amount of Fish: ")
		self.FishLabel.grid(row = 0, column = 0)

		self._FishBoxVar = StringVar()
		self._FishBox = Entry(self, textvariable = self._FishBoxVar)
		self._FishBox.grid(row = 0, column = 1)

		# Fish Breed Tick
		self.FishBreedLabel = Label(self, text="Enter the Fish Breed Tick: ")
		self.FishBreedLabel.grid(row = 1, column = 0)

		self._FishBreedBoxVar = StringVar()
		self._FishBreedBox = Entry(self, textvariable = self._FishBreedBoxVar)
		self._FishBreedBox.grid(row = 1, column = 1)

		# add to fish breed tick
		self._updateFishBreedAdd = Button(self,text = "+", command = self._addFishBreed)
		self._updateFishBreedAdd.grid(row = 1, column = 2)
		self._updateFishBreedAdd["state"] = DISABLED

		# subtract from fish breed tick
		self._updateFishBreedSub = Button(self,text = "-", command = self._subtractFishBreed)
		self._updateFishBreedSub.grid(row = 1, column = 3)
		self._updateFishBreedSub["state"] = DISABLED

		# Number of bears
		self.BearLabel = Label(self, text="Enter the amount of Bears: ")
		self.BearLabel.grid(row = 2, column = 0)

		self._BearBoxVar = StringVar()
		self._BearBox = Entry(self, textvariable = self._BearBoxVar)
		self._BearBox.grid(row = 2, column = 1)

		# Bear Breed Tick
		self.BearBreedLabel = Label(self, text="Enter the Bear Breed Tick: ")
		self.BearBreedLabel.grid(row = 3, column = 0)

		self._BearBreedBoxVar = StringVar()
		self._BearBreedBox = Entry(self, textvariable = self._BearBreedBoxVar)
		self._BearBreedBox.grid(row = 3, column = 1)

		# add to bear breed tick
		self._updateBearBreedAdd = Button(self,text = "+", command = self._addBearBreed)
		self._updateBearBreedAdd.grid(row = 3, column = 2)
		self._updateBearBreedAdd["state"] = DISABLED

		# subtract from bear breed tick
		self._updateBearBreedSub = Button(self,text = "-", command = self._subtractBearBreed)
		self._updateBearBreedSub.grid(row = 3, column = 3)
		self._updateBearBreedSub["state"] = DISABLED

		# Bear Starve Tick
		self.BearStarveLabel = Label(self, text="Enter the Bear Starve Tick: ")
		self.BearStarveLabel.grid(row = 4, column = 0)

		self._BearStarveBoxVar = StringVar()
		self._BearStarveBox = Entry(self, textvariable = self._BearStarveBoxVar)
		self._BearStarveBox.grid(row = 4, column = 1)

		# add to bear breed tick
		self._updateBearStarveAdd = Button(self,text = "+", command = self._addBearStarve)
		self._updateBearStarveAdd.grid(row = 4, column = 2)
		self._updateBearStarveAdd["state"] = DISABLED

		# subtract from bear breed tick
		self._updateBearStarveSub = Button(self,text = "-", command = self._subtractBearStarve)
		self._updateBearStarveSub.grid(row = 4, column = 3)
		self._updateBearStarveSub["state"] = DISABLED


		# World Timer
		self.WorldTimerLabel = Label(self, text="Enter the World Time: ")
		self.WorldTimerLabel.grid(row = 5, column = 0)

		self._WorldTimerBoxVar = StringVar()
		self._WorldTimerBox = Entry(self, textvariable = self._WorldTimerBoxVar)
		self._WorldTimerBox.grid(row = 5, column = 1)

		# World Width
		self.WorldWidthLabel = Label(self, text="Enter the World Width: ")
		self.WorldWidthLabel.grid(row = 6, column = 0)

		self._WorldWidthBoxVar = StringVar()
		self._WorldWidthBox = Entry(self, textvariable = self._WorldWidthBoxVar)
		self._WorldWidthBox.grid(row = 6, column = 1)

		# World Height
		self.WorldHeightLabel = Label(self, text="Enter the World Height: ")
		self.WorldHeightLabel.grid(row = 7, column = 0)

		self._WorldHeightBoxVar = StringVar()
		self._WorldHeightBox = Entry(self, textvariable = self._WorldHeightBoxVar)
		self._WorldHeightBox.grid(row = 7, column = 1)

		# Run Main Program
		self._RunMainButton = Button(self, text = "Run Environment", command = self._mainSimulation)
		self._RunMainButton.grid(row = 8, column = 1)
		self._RunMainButton["state"] = NORMAL

		# Number of current Bears
		self._NumberBearsBoxVar = StringVar()
		self._NumberBearsBox = Entry(self, textvariable = self._NumberBearsBoxVar, width = 30)
		self._NumberBearsBox.grid(row = 9, column = 0)

		# Number of current Fish
		self._NumberFishBoxVar = StringVar()
		self._NumberFishBox = Entry(self, textvariable = self._NumberFishBoxVar, width = 30)
		self._NumberFishBox.grid(row = 9, column = 1)

		# label for turtle speed
		self.TurtleSpeedLabel = Label(self, text="Update Turtle Speed: ")
		self.TurtleSpeedLabel.grid(row = 10, column = 0)

		# add speed to turtle
		self._updateTurtleSpeed = Button(self,text = "+", command = self._addTurtleSpeed)
		self._updateTurtleSpeed.grid(row = 11, column = 0)

		# subtract speed from turtle
		self._updateTurtleSpeed = Button(self,text = "-", command = self._subtractTurtleSpeed)
		self._updateTurtleSpeed.grid(row = 11, column = 1)

		# display speed of turtle
		self._TurtleSpeedBoxVar = StringVar()
		self._TurtleSpeedBox = Entry(self, textvariable = self._TurtleSpeedBoxVar, width = 30)
		self._TurtleSpeedBox.grid(row = 12, column = 0)

		self._Legend = Label(self,text = "Legend:")
		self._Legend.grid(row = 13, column = 0)

		self._FishLegendColor = Label(self,text = "Fish" , bg="red")
		self._FishLegendColor.grid(row = 14, column = 0)

		self._BearLegendColor = Label(self,text = "Bear", bg='brown')
		self._BearLegendColor.grid(row = 14, column = 1)

		self.IterationCheckLabel = Label(self, text="Current Iteration: ")
		self.IterationCheckLabel.grid(row = 15, column = 0)

		self._IterationCheckBoxVar = StringVar()
		self._IterationCheckBox = Entry(self, textvariable = self._IterationCheckBoxVar, width = 30)
		self._IterationCheckBox.grid(row = 15, column = 1)


	def _addTurtleSpeed(self):
		if self.turtleSpeed < 10:
			self.turtleSpeed = self.turtleSpeed + 1

	def _subtractTurtleSpeed(self):
		if self.turtleSpeed > 1:
			self.turtleSpeed = self.turtleSpeed - 1

	def _addFishBreed(self):
		self.fishBreedTick = self.fishBreedTick + 1

	def _subtractFishBreed(self):
		if self.fishBreedTick > 1:
			self.fishBreedTick = self.fishBreedTick - 1

	def _addBearBreed(self):
		self.bearBreedTick = self.bearBreedTick + 1

	def _subtractBearBreed(self):
		if self.bearBreedTick > 1:
			self.bearBreedTick = self.bearBreedTick - 1

	def _addBearStarve(self):
		self.bearStarveTick = self.bearStarveTick + 1

	def _subtractBearStarve(self):
		if self.bearStarveTick > 1:
			self.bearStarveTick = self.bearStarveTick - 1

	def _mainSimulation(self):
		self._RunMainButton["state"] = DISABLED
		self._updateFishBreedAdd["state"] = NORMAL
		self._updateFishBreedSub["state"] = NORMAL
		self._updateBearBreedAdd["state"] = NORMAL
		self._updateBearBreedSub["state"] = NORMAL
		self._updateBearStarveAdd["state"] = NORMAL
		self._updateBearStarveSub["state"] = NORMAL
		numberOfBears = int(self._BearBoxVar.get())
		numberOfFish = int(self._FishBoxVar.get())
		worldLifeTime = int(self._WorldTimerBoxVar.get())
		worldWidth = int(self._WorldWidthBoxVar.get())
		worldHeight = int(self._WorldHeightBoxVar.get())
		self.bearBreedTick = int(self._BearBreedBoxVar.get())
		self.fishBreedTick = int(self._FishBreedBoxVar.get())
		self.bearStarveTick = int(self._BearStarveBoxVar.get())

		myworld = World(worldWidth,worldHeight)
		myworld.draw()

		for i in range(numberOfFish):
			newFish = Fish()
			x = randrange(myworld.getMaxX())
			y = randrange(myworld.getMaxY())
			while not myworld.emptyLocation(x,y):
				x = randrange(myworld.getMaxX())
				y = randrange(myworld.getMaxY())
			myworld.addThing(newFish, x, y, self.fishBreedTick,0)

		for i in range(numberOfBears):
			newBear = Bear()
			x = randrange(myworld.getMaxX())
			y = randrange(myworld.getMaxY())
			while not myworld.emptyLocation(x,y):
				x = randrange(myworld.getMaxX())
				y = randrange(myworld.getMaxY())
			myworld.addThing(newBear, x, y, self.bearBreedTick,self.bearStarveTick)

		myData = [['timestamp', '#ofBears', '#ofFish']]
		myFile = open('FishBear.csv', 'w')
		with myFile:
	   		writer = csv.writer(myFile)
	   		writer.writerows(myData)

		for i in range(worldLifeTime):
			self._IterationCheckBoxVar.set(str(i))
			myworld.liveALittle()
			bearcounter = 0
			fishcounter = 0
			for i in range(len(myworld.thingList)):
				myworld.thingList[i].turtle.speed(self.turtleSpeed)
				self._TurtleSpeedBoxVar.set("The Current Speed of Turtles is: " + str(self.turtleSpeed))
				if isinstance(myworld.thingList[i],Fish):
					fishcounter = fishcounter + 1
					myworld.thingList[i].breedTickCounter = self.fishBreedTick
				elif isinstance(myworld.thingList[i],Bear):
					bearcounter = bearcounter + 1
					myworld.thingList[i].breedTickCounter = self.bearBreedTick
					myworld.thingList[i].starveTickCounter = self.bearStarveTick
			self._NumberFishBoxVar.set("The Number of Current Fish is: " + str(fishcounter))
			self._NumberBearsBoxVar.set("The Number of Current Bears is: " + str(bearcounter))
			self._FishBreedBoxVar.set(str(self.fishBreedTick))
			self._BearBreedBoxVar.set(str(self.bearBreedTick))
			self._BearStarveBoxVar.set(str(self.bearStarveTick))
			if fishcounter == 1 or bearcounter == 1:
				break

			myData = [[datetime.datetime.now(), bearcounter, fishcounter]]
			myFile = open('FishBear.csv', 'a')
			with myFile:
	   			writer = csv.writer(myFile)
	   			writer.writerows(myData)
		messagebox.showinfo(parent=self,message="Done!")
		myworld.freezeWorld()

def main():
	BearFishGUI().mainloop()
main()

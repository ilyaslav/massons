import RPi.GPIO as GPIO
import time

class PiHandler():
	def __init__(self):
		self.initGPIO()
		self.inputs = {
			'runQuest': True,
			'doorRead': True,
			'bookRead': True,
			'coinRead': True,
			'declarationRead': True,
			'brickRead': True,
			'handRead': True,
			'cupRead': True,
			'tableRead': True,
			'presidentRead': True,
			'ringRead': True,
			'playersRead': True
		}

	def sensors_loop(self):
		while True:
			try:
				if GPIO.input(3) != self.inputs['runQuest']:
					self.inputs['runQuest'] = GPIO.input(3)
					if self.inputs['runQuest']:
						self.runQuest0()
					else:
						self.runQuest1()

				if GPIO.input(5) != self.inputs['doorRead']:
					self.inputs['doorRead'] = GPIO.input(5)
					if self.inputs['doorRead']:
						self.doorRead0()
					else:
						self.doorRead1()

				if GPIO.input(7) != self.inputs['bookRead']:
					self.inputs['bookRead'] = GPIO.input(7)
					if self.inputs['bookRead']:
						self.bookRead0()
					else:
						self.bookRead1()

				if GPIO.input(11) != self.inputs['coinRead']:
					self.inputs['coinRead'] = GPIO.input(11)
					if self.inputs['coinRead']:
						self.coinRead0()
					else:
						self.coinRead1()

				if GPIO.input(13) != self.inputs['declarationRead']:
					self.inputs['declarationRead'] = GPIO.input(13)
					if self.inputs['declarationRead']:
						self.declarationRead0()
					else:
						self.declarationRead1()

				if GPIO.input(15) != self.inputs['brickRead']:
					self.inputs['brickRead'] = GPIO.input(15)
					if self.inputs['brickRead']:
						self.brickRead0()
					else:
						self.brickRead1()

				if GPIO.input(19) != self.inputs['handRead']:
					self.inputs['handRead'] = GPIO.input(19)
					if self.inputs['handRead']:
						self.handRead0()
					else:
						self.handRead1()

				if GPIO.input(21) != self.inputs['cupRead']:
					self.inputs['cupRead'] = GPIO.input(21)
					if self.inputs['cupRead']:
						self.cupRead0()
					else:
						self.cupRead1()

				if GPIO.input(23) != self.inputs['tableRead']:
					self.inputs['tableRead'] = GPIO.input(23)
					if self.inputs['tableRead']:
						self.tableRead0()
					else:
						self.tableRead1()

				if GPIO.input(29) != self.inputs['presidentRead']:
					self.inputs['presidentRead'] = GPIO.input(29)
					if self.inputs['presidentRead']:
						self.presidentRead0()
					else:
						self.presidentRead1()

				if GPIO.input(31) != self.inputs['ringRead']:
					self.inputs['ringRead'] = GPIO.input(31)
					if self.inputs['ringRead']:
						self.ringRead0()
					else:
						self.ringRead1()

				if GPIO.input(33) != self.inputs['playersRead']:
					self.inputs['playersRead'] = GPIO.input(33)
					if self.inputs['playersRead']:
						self.playersRead0()
					else:
						self.playersRead1()

				time.sleep(0.1)
			except:
				pass

	def initGPIO(self):
		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(29, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(31, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		GPIO.setup(33, GPIO.IN, pull_up_down = GPIO.PUD_UP)

		GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(32, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(36, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(38, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(40, GPIO.OUT, initial=GPIO.HIGH)
		GPIO.setup(37, GPIO.OUT, initial=GPIO.HIGH)

	def hallway1(self):
		GPIO.output(8, GPIO.LOW)
	def hallway0(self):
		GPIO.output(8, GPIO.HIGH)
	def room11(self):
		GPIO.output(10, GPIO.HIGH)
	def room10(self):
		GPIO.output(10, GPIO.LOW)
	def coin1(self):
		GPIO.output(12, GPIO.LOW)
	def coin0(self):
		GPIO.output(12, GPIO.HIGH)
	def declaration1(self):
		GPIO.output(16, GPIO.LOW)
	def declaration0(self):
		GPIO.output(16, GPIO.HIGH)
	def brick1(self):
		GPIO.output(18, GPIO.HIGH)
	def brick0(self):
		GPIO.output(18, GPIO.LOW)
	def stones1(self):
		GPIO.output(22, GPIO.LOW)
	def stones0(self):
		GPIO.output(22, GPIO.HIGH)
	def room21(self):
		GPIO.output(24, GPIO.LOW)
	def room20(self):
		GPIO.output(24, GPIO.HIGH)
	def left1(self):
		GPIO.output(26, GPIO.LOW)
	def left0(self):
		GPIO.output(26, GPIO.HIGH)
	def table1(self):
		GPIO.output(32, GPIO.LOW)
	def table0(self):
		GPIO.output(32, GPIO.HIGH)
	def right1(self):
		GPIO.output(36, GPIO.LOW)
	def right0(self):
		GPIO.output(36, GPIO.HIGH)
	def room31(self):
		GPIO.output(38, GPIO.LOW)
	def room30(self):
		GPIO.output(38, GPIO.HIGH)
	def under1(self):
		GPIO.output(40, GPIO.LOW)
	def under0(self):
		GPIO.output(40, GPIO.HIGH)
	def input1(self):
		GPIO.output(37, GPIO.LOW)
	def input0(self):
		GPIO.output(37, GPIO.HIGH)


	def runQuest1(self):
		pass
	def runQuest0(self):
		pass
	def doorRead1(self):
		pass
	def doorRead0(self):
		pass
	def bookRead1(self):
		pass
	def bookRead0(self):
		pass
	def coinRead1(self):
		pass
	def coinRead0(self):
		pass
	def declarationRead1(self):
		pass
	def declarationRead0(self):
		pass
	def brickRead1(self):
		pass
	def brickRead0(self):
		pass
	def handRead1(self):
		pass
	def handRead0(self):
		pass
	def cupRead1(self):
		pass
	def cupRead0(self):
		pass
	def tableRead1(self):
		pass
	def tableRead0(self):
		pass
	def presidentRead1(self):
		pass
	def presidentRead0(self):
		pass
	def ringRead1(self):
		pass
	def ringRead0(self):
		pass
	def playersRead1(self):
		pass
	def playersRead0(self):
		pass
	
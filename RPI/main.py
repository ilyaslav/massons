from _client import Client
from _gpio import PiHandler
from _music import Music
import threading

class GameHandler(PiHandler):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def runQuest1(self):
		gc.send_message('quest1;')
	def runQuest0(self):
		gc.send_message('quest0;')
	def doorRead1(self):
		gc.send_message('door1;')
	def doorRead0(self):
		gc.send_message('door0;')
	def bookRead1(self):
		gc.send_message('book1;')
	def bookRead0(self):
		gc.send_message('book0;')
	def coinRead1(self):
		gc.send_message('coin1;')
	def coinRead0(self):
		gc.send_message('coin0;')
	def declarationRead1(self):
		gc.send_message('decl1;')
	def declarationRead0(self):
		gc.send_message('decl0;')
	def brickRead1(self):
		gc.send_message('bric1;')
	def brickRead0(self):
		gc.send_message('bric0;')
	def handRead1(self):
		gc.send_message('hand1;')
	def handRead0(self):
		gc.send_message('hand0;')
	def cupRead1(self):
		gc.send_message('cupr1;')
	def cupRead0(self):
		gc.send_message('cupr0;')
	def tableRead1(self):
		gc.send_message('tabl1;')
	def tableRead0(self):
		gc.send_message('tabl0;')
	def presidentRead1(self):
		gc.send_message('pres1;')
	def presidentRead0(self):
		gc.send_message('pres0;')
	def ringRead1(self):
		gc.send_message('ring1;')
	def ringRead0(self):
		gc.send_message('ring0;')
	def playersRead1(self):
		gc.send_message('play1;')
	def playersRead0(self):
		gc.send_message('play0;')


class GameClient(Client):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def messageHandler(self, mes):
		if mes == 'hallway1':
			gh.hallway1()
		elif mes == 'room11':
			gh.room11()
		elif mes == 'coin1':
			gh.coin1()
		elif mes == 'declaration1':
			gh.declaration1()
		elif mes == 'brick1':
			gh.brick1()
		elif mes == 'stones1':
			gh.stones1()
		elif mes == 'room21':
			gh.room21()
		elif mes == 'left1':
			gh.left1()
		elif mes == 'table1':
			gh.table1()
		elif mes == 'right1':
			gh.right1()
		elif mes == 'room31':
			gh.room31()
		elif mes == 'under1':
			gh.under1()
		elif mes == 'input1':
			gh.input1()

		if mes == 'hallway0':
			gh.hallway0()
		elif mes == 'room10':
			gh.room10()
		elif mes == 'coin0':
			gh.coin0()
		elif mes == 'declaration0':
			gh.declaration0()
		elif mes == 'brick0':
			gh.brick0()
		elif mes == 'stones0':
			gh.stones0()
		elif mes == 'room20':
			gh.room20()
		elif mes == 'left0':
			gh.left0()
		elif mes == 'table0':
			gh.table0()
		elif mes == 'right0':
			gh.right0()
		elif mes == 'room30':
			gh.room30()
		elif mes == 'under0':
			gh.under0()
		elif mes == 'input0':
			gh.input0()

		elif mes[:4] == 'play':
			gm.play(int(mes[4:]))
		elif mes[:4] == 'stop':
			gm.stop(int(mes[4:]))
		elif mes[:5] == 'pause':
			gm.pause(int(mes[5:]))
		elif mes[:6] == 'volume':
			gm.change_volume(int(mes[6:]))


gc = GameClient()
gh = GameHandler()
gm = Music()


def main():
	threading.Thread(target=gc.clientFunction, daemon=True).start()
	gh.sensors_loop()


if __name__ == '__main__':
	main()
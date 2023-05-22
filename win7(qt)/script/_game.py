from _server import Server
import threading
import time
import _time

class GameServer(Server):
	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)

	def message_handler(self, mes):
		if mes == 'quest1':
			inputs['runQuest'] = True
			if not settings['gameStatus']:
				start_timer()
		elif mes == 'quest0':
			inputs['runQuest'] = False
			if not settings['gameStatus']:
				stop_timer()
		if mes == 'door1':
			inputs['doorRead'] = True
			playerInput_script()
		elif mes == 'door0':
			inputs['doorRead'] = False
			win_script()
		if mes == 'book1':
			inputs['bookRead'] = True
			book_script()
		elif mes == 'book0':
			inputs['bookRead'] = False
		if mes == 'coin1':
			inputs['coinRead'] = True
			coin_script()
		elif mes == 'coin0':
			inputs['coinRead'] = False
		if mes == 'decl1':
			inputs['declarationRead'] = True
			declaration_script()
		elif mes == 'decl0':
			inputs['declarationRead'] = False
		if mes == 'bric1':
			inputs['brickRead'] = True
			brick_script()
		elif mes == 'bric0':
			inputs['brickRead'] = False
		if mes == 'hand1':
			inputs['handRead'] = True
			hand_script()
		elif mes == 'hand0':
			inputs['handRead'] = False
		if mes == 'cupr1':
			inputs['cupRead'] = True
			cup_script()
		elif mes == 'cupr0':
			inputs['cupRead'] = False
		if mes == 'tabl1':
			inputs['tableRead'] = True
			table_script()
		elif mes == 'tabl0':
			inputs['tableRead'] = False
		if mes == 'pres1':
			inputs['presidentRead'] = True
			president_script()
		elif mes == 'pres0':
			inputs['presidentRead'] = False
		if mes == 'ring1':
			inputs['ringRead'] = True
			ring_script()
		elif mes == 'ring0':
			inputs['ringRead'] = False
		if mes == 'play1':
			inputs['playersRead'] = True
			players_script()
		elif mes == 'play0':
			inputs['playersRead'] = False

	def send_message(self, message):
		for conn in self.connection:
			try:
				conn.send(message.encode('utf-8'))
			except:
				self.connection.pop()

gs = GameServer()
threading.Thread(target=gs.serverFunction, daemon=True).start()

settings = {
	'gameStatus': False,
	'startStatus': False,
	'questStatus': 2,
	'initSensors': False,
	'volume': 0,
	'brick_event': True,
	'players_event': False,	
	'timer': False,
	'start_time': 0
}

inputs = {
	'runQuest': False,
	'doorRead': False,
	'bookRead': False,
	'coinRead': False,
	'declarationRead': False,
	'brickRead': False,
	'handRead': False,
	'cupRead': False,
	'tableRead': False,
	'presidentRead': False,
	'ringRead': False,
	'playersRead': False
}

outs = {
	'hallway': False,
	'room1': False,
	'coin': False,
	'declaration': False,
	'brick': False,
	'stones': False,
	'room2': False,
	'left': False,
	'table': False,
	'right': False,
	'room3': False,
	'under': False,
	'input': False,
}

def check_sensors():
	for i in inputs:
		if inputs[i]:
			return False
	return True

def check_outs():
	for i in outs:
		if outs[i]:
			return False
	return True

def check():
	return check_sensors() and check_outs()

def chouse_track(music):
	if music == 'Трек №1  «Райли»':
		return 1
	elif music == 'Трек №2  «1-я комната»':
		return 2
	elif music == 'Трек №3  «2-я комната»':
		return 3
	elif music == 'Трек №4  «3-я комната»':
		return 4
	elif music == 'Трек №5  «Сигнализация»':
		return 5
	elif music == 'Трек №6  «Побег»':
		return 6
	elif music == 'Трек №7  «Победа»':
		return 7
	elif music == 'Трек №8  «Поражение»':
		return 8
	elif music == 'Трек №9  «Alarm»':
		return 9
	return 0

def play_music(music):
	track = chouse_track(music)
	gs.send_message(f'play{track};')

def pause_music(music):
	track = chouse_track(music)
	gs.send_message(f'pause{track};')

def stop_music(music):
	track = chouse_track(music)
	gs.send_message(f'stop{track};')

def change_volume():
	gs.send_message(f'volume{int(settings["volume"])};')
	print(settings["volume"])

def reset_out(message):
	if outs[message]:
		gs.send_message(f'{message}1;')
	else:
		gs.send_message(f'{message}0;')

def start_timer():
	if not settings['timer']:
		settings['timer'] = True
		settings['start_time'] = time.time()

def stop_timer():
	if time.time() - settings['start_time'] > 2 and time.time() - settings['start_time'] < 5:
		settings['startStatus'] = True
	settings['timer'] = False

def start_script():
	outs['hallway'] = True
	reset_out('hallway')
	play_music('Трек №1  «Райли»')

def playerInput_script():
	if not outs['room1'] or outs['under']:
		outs['hallway'] = False
		reset_out('hallway')
		outs['room1'] = True
		reset_out('room1')
		stop_music('Трек №1  «Райли»')
		play_music('Трек №2  «1-я комната»')

def book_script():
	outs['coin'] = True
	reset_out('coin')

def coin_script():
	outs['declaration'] = True
	reset_out('declaration')

def declaration_script():
	outs['brick'] = True
	settings['brick_event'] = True
	reset_out('brick')

def brick_script():
	outs['stones'] = True
	reset_out('stones')

def hand_script():
	outs['room2'] = True
	reset_out('room2')
	stop_music('Трек №2  «1-я комната»')
	play_music('Трек №3  «2-я комната»')

def cup_script():
	outs['left'] = True
	reset_out('left')

def table_script():
	outs['table'] = True
	reset_out('table')

def president_script():
	outs['right'] = True
	reset_out('right')

def ring_script():
	outs['room3'] = True
	reset_out('room3')
	stop_music('Трек №3  «2-я комната»')
	play_music('Трек №4  «3-я комната»')

def players_script():
	outs['under'] = True
	reset_out('under')
	settings['players_event'] = True

def playersEvent_script(type):
	if type == 1:
		stop_music('Трек №4  «3-я комната»')
		play_music('Трек №5  «Сигнализация»')
	elif type == 2:
		stop_music('Трек №5  «Сигнализация»')
		play_music('Трек №6  «Побег»')

def win_script():
	if not inputs['doorRead'] and outs['room3']:
		settings['questStatus'] = 4
		settings['gameStatus'] = False
		stop_music('Трек №6  «Побег»')
		play_music('Трек №7  «Победа»')

def louse_script():
	settings['gameStatus'] = False
	outs['input'] = True
	reset_out('input')
	stop_music('Трек №6  «Побег»')
	play_music('Трек №8  «Поражение»')
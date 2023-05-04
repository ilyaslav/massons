gameStatus = False
questStatus = 2
initSensors = False
volume = 0

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

def play_music(music):
	pass

def pause_music(music):
	pass

def stop_music(music):
	pass
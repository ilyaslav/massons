time = 0
time_limit = 3600

def get_hours(_time):
	hours = int(_time / 3600)
	if hours < 10:
		return f'0{hours}'
	else:
		return f'{hours}'

def get_minutes(_time):
	minutes = int((_time % 3600) / 60)
	if minutes < 10:
		return f'0{minutes}'
	else:
		return f'{minutes}'

def get_seconds(_time):
	seconds = _time % 60
	if seconds < 10:
		return f'0{seconds}'
	else:
		return f'{seconds}'

def get_progress():
	return int(time/time_limit*100)
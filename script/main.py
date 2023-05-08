from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'height', '900')
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'resizable', '1')
Config.write()

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image 
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label

from kivy.core.window import Window
from kivy.clock import Clock
from functools import partial

from kivy.graphics import *

import _time
import _game

class MassonsApp(App):
	def build(self):
		self.mw = MainWindow()

		self.iw = InputWindow(size_hint_x = 0.4)
		self.ow = OutputWindow(size_hint_x = 0.6)
		self.mw.add_widget(self.iw)
		self.mw.add_widget(self.ow)

		Clock.schedule_once(self.start, 0)

		return self.mw

	def main_loop(self, dt):
		if _game.settings['questStatus'] == 4:
			self.ow.timer_on.cancel()
			self.ow.bt_initQuest.disabled = False

		if _game.settings['initSensors']:
			self.iw.init_sensors()
		self.iw.reset_sensors()
		self.ow.reset_outs()

		if not _game.check() and not _game.settings['gameStatus'] and _game.settings['questStatus'] != 4:
			_game.settings['questStatus'] = 1
		elif _game.check() and not _game.settings['gameStatus'] and _game.settings['questStatus'] != 4:
			_game.settings['questStatus'] = 2

		if _game.outs['brick'] and _game.settings['brick_event']:
			_game.settings['brick_event'] = False
			self.ow.brick_event = Clock.schedule_once(self.ow.bt_brickOff_press, 3)

		if _game.settings['players_event']:
			_game.settings['players_event'] = False
			Clock.schedule_once(partial(_game.playersEvent_script, 1), 5)
			Clock.schedule_once(partial(_game.playersEvent_script, 2), 20)

		if _game.settings['startStatus']:
			_game.settings['startStatus'] = False
			_game.settings['gameStatus'] = not _game.settings['gameStatus']

			self.ow.bt_initQuest.disabled = not self.ow.bt_initQuest.disabled
			if _game.settings['gameStatus']:
				_game.start_script()
				_game.settings['questStatus'] = 3
				self.ow.timer_on = Clock.schedule_interval(self.ow.timer_run, 1)
			else:
				_game.settings['questStatus'] = 4
				self.ow.timer_on.cancel()
	
		self.ow.change_quest_state_text()
		self.ow.change_quest_state_color()

	def start(self, dt):
		Clock.schedule_interval(self.main_loop, 0.1)


class MainWindow(BoxLayout):
	pass


class InputWindow(BoxLayout):
	def reset_sensors(self):
		if _game.inputs['runQuest']:
			self.green_sensor(self.run)
		else:
			self.red_sensor(self.run)

		if _game.inputs['doorRead']:
			self.green_sensor(self.door)
		else:
			self.red_sensor(self.door)

		if _game.inputs['bookRead']:
			self.green_sensor(self.book)

		if _game.inputs['coinRead']:
			self.green_sensor(self.coin)

		if _game.inputs['declarationRead']:
			self.green_sensor(self.declaration)

		if _game.inputs['brickRead']:
			self.green_sensor(self.brick)

		if _game.inputs['handRead']:
			self.green_sensor(self.hand)

		if _game.inputs['cupRead']:
			self.green_sensor(self.cup)

		if _game.inputs['tableRead']:
			self.green_sensor(self.table)

		if _game.inputs['presidentRead']:
			self.green_sensor(self.president)

		if _game.inputs['ringRead']:
			self.green_sensor(self.ring)

		if _game.inputs['playersRead']:
			self.green_sensor(self.players)
		else:
			self.red_sensor(self.players)

	def init_sensors(self):
		if _game.inputs['runQuest']:
			self.green_sensor(self.run)
		else:
			self.red_sensor(self.run)

		if _game.inputs['doorRead']:
			self.green_sensor(self.door)
		else:
			self.red_sensor(self.door)

		if _game.inputs['bookRead']:
			self.green_sensor(self.book)
		else:
			self.red_sensor(self.book)

		if _game.inputs['coinRead']:
			self.green_sensor(self.coin)
		else:
			self.red_sensor(self.coin)

		if _game.inputs['declarationRead']:
			self.green_sensor(self.declaration)
		else:
			self.red_sensor(self.declaration)

		if _game.inputs['brickRead']:
			self.green_sensor(self.brick)
		else:
			self.red_sensor(self.brick)

		if _game.inputs['handRead']:
			self.green_sensor(self.hand)
		else:
			self.red_sensor(self.hand)

		if _game.inputs['cupRead']:
			self.green_sensor(self.cup)
		else:
			self.red_sensor(self.cup)

		if _game.inputs['tableRead']:
			self.green_sensor(self.table)
		else:
			self.red_sensor(self.table)

		if _game.inputs['presidentRead']:
			self.green_sensor(self.president)
		else:
			self.red_sensor(self.president)

		if _game.inputs['ringRead']:
			self.green_sensor(self.ring)
		else:
			self.red_sensor(self.ring)

		if _game.inputs['playersRead']:
			self.green_sensor(self.players)
		else:
			self.red_sensor(self.players)

		_game.initSensors = False

	def green_sensor(self, sensor):
		sensor.canvas.before.clear()
		with sensor.canvas.before:
			Color(0,1,0,1)
			Rectangle(size = sensor.size, pos = sensor.pos)

	def red_sensor(self, sensor):
		sensor.canvas.before.clear()
		with sensor.canvas.before:
			Color(1,0,0,1)
			Rectangle(size = sensor.size, pos = sensor.pos)
			Color(1,0.99,0.93,1)
			Rectangle(size = (sensor.width - 16, sensor.height - 16), pos = (sensor.x + 8, sensor.y + 8))

class OutputWindow(BoxLayout):
	def change_quest_state_text(self):
		if _game.settings['questStatus'] == 1:
			self.quest_state.text = 'Квест не собран'
		elif _game.settings['questStatus'] == 2:
			self.quest_state.text = 'Квест собран'
		elif _game.settings['questStatus'] == 3:
			self.quest_state.text = 'Квест запущен'
		elif _game.settings['questStatus'] == 4:
			self.quest_state.text = 'Квест окончен'

	def change_quest_state_color(self):
		self.quest_state.canvas.before.clear()
		with self.quest_state.canvas.before:
			if _game.settings['questStatus'] == 1:
				Color(1,0,0,1)
			elif _game.settings['questStatus'] == 2:
				Color(0,1,0,1)
			elif _game.settings['questStatus'] == 3:
				Color(1,1,0,1)
			elif _game.settings['questStatus'] == 4:
				Color(0.26,0.67,1,1)
			Rectangle(size = self.quest_state.size, pos = self.quest_state.pos)

	def bt_runQuest_press(self):
		_game.settings['startStatus'] = True

	def bt_initQuest_press(self):
		_time.time = 0
		_time.time_limit = 3600
		self.reset_time()
		self.reset_progressbar()

		_game.settings['initSensors'] = True
		_game.settings['questStatus'] = 1

	def open_dd(self):
		dropdown = CustomDropDown()
		dropdown.container.spacing = 1
		dropdown.container.padding = 1
		dropdown.open(self.bt_songs)
		dropdown.bind(on_select=lambda instance, x: setattr(self.bt_songs, 'text', x))

	def bt_play_press(self):
		_game.play_music(self.bt_songs.text)

	def bt_pause_press(self):
		_game.pause_music(self.bt_songs.text)

	def bt_stop_press(self):
		_game.stop_music(self.bt_songs.text)

	def bt_alarm_press(self):
		_game.play_music('Трек №9  «Alarm»')

	def slider_move(self):
		if _game.settings['volume']!= self.slider.value:
			_game.settings['volume'] = self.slider.value
			_game.change_volume()

	def timer_run(self, dt):
		_time.time += 1
		self.reset_time()
		self.reset_progressbar()

		if _time.time == _time.time_limit:
			self.timer_on.cancel()
			_game.settings['questStatus'] = 4
			_game.louse_script()

	def reset_time(self):
		self.timer.text = f'Времени квеста прошло: '+\
		f'{_time.get_hours(_time.time)}:{_time.get_minutes(_time.time)}:{_time.get_seconds(_time.time)} / '+\
		f'{_time.get_hours(_time.time_limit)}:{_time.get_minutes(_time.time_limit)}:{_time.get_seconds(_time.time_limit)}'+\
		f'  ({_time.get_progress()}%)'

	def reset_progressbar(self):
		self.progressbar.max = _time.time_limit
		self.progressbar.value = _time.time

	def bt_m3min_press(self):
		if _time.time_limit > 3600:
			_time.time_limit -= 180
		self.reset_time()

	def bt_3min_press(self):
		_time.time_limit += 180
		self.reset_time()

	def bt_hallwayOn_press(self):
		_game.outs['hallway'] = True
		self.bt_hallwayOn.background_color = '00ff00ff'
		_game.reset_out('hallway')

	def bt_hallwayOff_press(self):
		_game.outs['hallway'] = False
		self.bt_hallwayOn.background_color = 'fffceeff'
		_game.reset_out('hallway')

	def bt_room1On_press(self):
		_game.outs['room1'] = True
		self.bt_room1On.background_color = '00ff00ff'
		_game.reset_out('room1')

	def bt_room1Off_press(self):
		_game.outs['room1'] = False
		self.bt_room1On.background_color = 'fffceeff'
		_game.reset_out('room1')

	def bt_coinOn_press(self):
		_game.outs['coin'] = True
		self.bt_coinOn.background_color = '00ff00ff'
		_game.reset_out('coin')

	def bt_coinOff_press(self):
		_game.outs['coin'] = False
		self.bt_coinOn.background_color = 'fffceeff'
		_game.reset_out('coin')

	def bt_declarationOn_press(self):
		_game.outs['declaration'] = True
		self.bt_declarationOn.background_color = '00ff00ff'
		_game.reset_out('declaration')

	def bt_declarationOff_press(self):
		_game.outs['declaration'] = False
		self.bt_declarationOn.background_color = 'fffceeff'
		_game.reset_out('declaration')

	def bt_brickOn_press(self):
		_game.outs['brick'] = True
		self.bt_brickOn.background_color = '00ff00ff'
		_game.reset_out('brick')
		_game.settings['brick_event'] = True

	def bt_brickOff_press(self, dt):
		_game.outs['brick'] = False
		self.bt_brickOn.background_color = 'fffceeff'
		_game.reset_out('brick')

	def bt_stonesOn_press(self):
		_game.outs['stones'] = True
		self.bt_stonesOn.background_color = '00ff00ff'
		_game.reset_out('stones')

	def bt_stonesOff_press(self):
		_game.outs['stones'] = False
		self.bt_stonesOn.background_color = 'fffceeff'
		_game.reset_out('stones')

	def bt_room2On_press(self):
		_game.outs['room2'] = True
		self.bt_room2On.background_color = '00ff00ff'
		_game.reset_out('room2')

	def bt_room2Off_press(self):
		_game.outs['room2'] = False
		self.bt_room2On.background_color = 'fffceeff'
		_game.reset_out('room2')

	def bt_leftOn_press(self):
		_game.outs['left'] = True
		self.bt_leftOn.background_color = '00ff00ff'
		_game.reset_out('left')

	def bt_leftOff_press(self):
		_game.outs['left'] = False
		self.bt_leftOn.background_color = 'fffceeff'
		_game.reset_out('left')

	def bt_tableOn_press(self):
		_game.outs['table'] = True
		self.bt_tableOn.background_color = '00ff00ff'
		_game.reset_out('table')

	def bt_tableOff_press(self):
		_game.outs['table'] = False
		self.bt_tableOn.background_color = 'fffceeff'
		_game.reset_out('table')

	def bt_rightOn_press(self):
		_game.outs['right'] = True
		self.bt_rightOn.background_color = '00ff00ff'
		_game.reset_out('right')

	def bt_rightOff_press(self):
		_game.outs['right'] = False
		self.bt_rightOn.background_color = 'fffceeff'
		_game.reset_out('right')

	def bt_room3On_press(self):
		_game.outs['room3'] = True
		self.bt_room3On.background_color = '00ff00ff'
		_game.reset_out('room3')

	def bt_room3Off_press(self):
		_game.outs['room3'] = False
		self.bt_room3On.background_color = 'fffceeff'
		_game.reset_out('room3')

	def bt_underOn_press(self):
		_game.outs['under'] = True
		self.bt_underOn.background_color = '00ff00ff'
		_game.reset_out('under')

	def bt_underOff_press(self):
		_game.outs['under'] = False
		self.bt_underOn.background_color = 'fffceeff'
		_game.reset_out('under')

	def bt_inputOn_press(self):
		_game.outs['input'] = True
		self.bt_inputOn.background_color = '00ff00ff'
		_game.reset_out('input')

	def bt_inputOff_press(self):
		_game.outs['input'] = False
		self.bt_inputOn.background_color = 'fffceeff'
		_game.reset_out('input')

	def reset_outs(self):
		if _game.outs['hallway'] == True:
			self.bt_hallwayOn.background_color = '00ff00ff'
		else:
			self.bt_hallwayOn.background_color = 'fffceeff'
		if _game.outs['room1'] == True:
			self.bt_room1On.background_color = '00ff00ff'
		else:
			self.bt_room1On.background_color = 'fffceeff'
		if _game.outs['coin'] == True:
			self.bt_coinOn.background_color = '00ff00ff'
		else:
			self.bt_coinOn.background_color = 'fffceeff'
		if _game.outs['declaration'] == True:
			self.bt_declarationOn.background_color = '00ff00ff'
		else:
			self.bt_declarationOn.background_color = 'fffceeff'
		if _game.outs['brick'] == True:
			self.bt_brickOn.background_color = '00ff00ff'
		else:
			self.bt_brickOn.background_color = 'fffceeff'
		if _game.outs['stones'] == True:
			self.bt_stonesOn.background_color = '00ff00ff'
		else:
			self.bt_stonesOn.background_color = 'fffceeff'
		if _game.outs['room2'] == True:
			self.bt_room2On.background_color = '00ff00ff'
		else:
			self.bt_room2On.background_color = 'fffceeff'
		if _game.outs['left'] == True:
			self.bt_leftOn.background_color = '00ff00ff'
		else:
			self.bt_leftOn.background_color = 'fffceeff'
		if _game.outs['table'] == True:
			self.bt_tableOn.background_color = '00ff00ff'
		else:
			self.bt_tableOn.background_color = 'fffceeff'
		if _game.outs['right'] == True:
			self.bt_rightOn.background_color = '00ff00ff'
		else:
			self.bt_rightOn.background_color = 'fffceeff'
		if _game.outs['room3'] == True:
			self.bt_room3On.background_color = '00ff00ff'
		else:
			self.bt_room3On.background_color = 'fffceeff'
		if _game.outs['under'] == True:
			self.bt_underOn.background_color = '00ff00ff'
		else:
			self.bt_underOn.background_color = 'fffceeff'
		if _game.outs['input'] == True:
			self.bt_inputOn.background_color = '00ff00ff'
		else:
			self.bt_inputOn.background_color = 'fffceeff'
			


class CustomDropDown(DropDown):
	pass


def main():
	MassonsApp().run()

if __name__ == '__main__':
	main()
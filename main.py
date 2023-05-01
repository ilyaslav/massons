from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.image import Image 
from kivy.uix.dropdown import DropDown

class MassonsApp(App):
	def build(self):
		bl = BoxLayout()
		widget = ImageWidget()
		bl.add_widget(widget)
		bl.add_widget(Tab())
		return bl


class Tab(TabbedPanel):
	def open_dd(self):
		dropdown = CustomDropDown()
		dropdown.open(self.bt_songs)
		dropdown.bind(on_select=lambda instance, x: setattr(self.bt_songs, 'text', x))

class CustomDropDown(DropDown):
	pass


class ImageWidget(Image):
	def __init__(self, **kwargs):
		super(ImageWidget, self).__init__(**kwargs)



def main():
	MassonsApp().run()

if __name__ == '__main__':
	main()
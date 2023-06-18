from audioplayer import AudioPlayer
import alsaaudio

class Music():
	def __init__(self):
		self.ap1 = AudioPlayer('/home/user/Desktop/RPI/mp3/1.mp3')
		self.ap2 = AudioPlayer('/home/user/Desktop/RPI/mp3/2.mp3')
		self.ap3 = AudioPlayer('/home/user/Desktop/RPI/mp3/3.mp3')
		self.ap4 = AudioPlayer('/home/user/Desktop/RPI/mp3/4.mp3')
		self.ap5 = AudioPlayer('/home/user/Desktop/RPI/mp3/5.mp3')
		self.ap6 = AudioPlayer('/home/user/Desktop/RPI/mp3/6.mp3')
		self.ap7 = AudioPlayer('/home/user/Desktop/RPI/mp3/7.mp3')
		self.ap8 = AudioPlayer('/home/user/Desktop/RPI/mp3/8.mp3')
		self.ap9 = AudioPlayer('/home/user/Desktop/RPI/mp3/9.mp3')

		self.tracks = [False, False, False,\
		 False, False, False, False, False, False]

		self.mix = alsaaudio.Mixer()

	def change_volume(self, vol):
		self.mix.setvolume(vol)

	def play(self, track):
		if self.tracks[track - 1]:
			self.chouse_track(track).resume()
		else:
			self.chouse_track(track).play()
		self.tracks[track - 1] = False
	
	def stop(self, track):
		self.tracks[track - 1] = False
		self.chouse_track(track).play()
		self.chouse_track(track).stop()
	
	def pause(self, track):
		self.tracks[track - 1] = True
		self.chouse_track(track).pause()

	def chouse_track(self, music):
		if music == 1:
			return self.ap1
		elif music == 2:
			return self.ap2
		elif music == 3:
			return self.ap3
		elif music == 4:
			return self.ap4
		elif music == 5:
			return self.ap5
		elif music == 6:
			return self.ap6
		elif music == 7:
			return self.ap7
		elif music == 8:
			return self.ap8
		else:
			return self.ap9

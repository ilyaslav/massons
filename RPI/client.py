#import RPi.GPIO as GPIO
import socket
import threading

class Client:
	def __init__(self):
		self.server = []
		self.messages = []
		self.HOST = "192.168.0."
		self.PORT = 1112

	def clientFunction(self):
		i = 0
		while True:
			try:
				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
					s.settimeout(0.01)
					print(self.HOST+f'{i}')
					s.connect((self.HOST+f'{i}', self.PORT))
					s.settimeout(None)
					self.server.append(s)

					while True:
						data = s.recv(1024).decode('utf-8')
						self.messages.extend(data.split(';')[:-1])

						while self.messages:
							self.messageHandler(self.messages.pop(0))

			except TimeoutError as e:
				print(i)
				if i == 254:
					i = 1
				else:
					i+=1

				if self.server:
					self.server.pop()
				continue
					
			except OSError as e:
				print(e)
				if i == 254:
					i = 1
				else:
					i+=1

				if self.server:
					self.server.pop()
				s.close()

	def send_message(self, message):
		for s in self.server:
			try:
				s.send(message.encode('utf-8'))
			except:
				self.server.pop()

	def set_default_settings(self):
		pass

	def messageHandler(self, message):
		print(message)

if __name__ == "__main__":
	client = Client()
	threading.Thread(target=client.clientFunction, daemon=True).start()
	while True:
		client.send_message(input())

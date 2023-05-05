import socket

class Server():
	def __init__(self):
		self.connection = []
		self.messenges = []
		self.HOST = socket.gethostbyname(socket.gethostname())
		self.PORT = 1112

	def serverFunction(self):	
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((self.HOST,self.PORT))
			s.listen()

			while True:
				try:
					conn, addr = s.accept()
					with conn:
						self.connection.append(conn)
						print(f"Connected by {addr}")
						print(self.connection)
			
						while True:
							data = conn.recv(1024).decode('utf-8')
							self.messenges.extend(data.split(';')[:-1])

							while self.messenges:
								ms = self.messenges.pop()

								self.message_handler(ms)


				except TimeoutError as e:
					print(e)
					continue
			
				except OSError as e:
					print(e)
					self.connection.pop()

	def message_handler(self, mes):
		pass
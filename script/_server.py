import socket

class Server():
	def __init__(self):
		self.connection = []
		self.messenges = []
		self.HOST = self.get_local_ip()
		#self.HOST = socket.gethostbyname(socket.gethostname())
		print(self.HOST)
		self.PORT = 1112

	def get_local_ip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			# doesn't even have to be reachable
			s.connect(('192.255.255.255', 1))
			IP = s.getsockname()[0]
		except:
			IP = '127.0.0.1'
		finally:
			s.close()
		return IP

	def serverFunction(self):	
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((self.HOST,self.PORT))
			s.listen()

			while True:
				try:
					conn, addr = s.accept()
					with conn:
						self.connection.append(conn)
			
						while True:
							data = conn.recv(1024).decode('utf-8')
							self.messenges.extend(data.split(';')[:-1])

							while self.messenges:
								ms = self.messenges.pop()

								self.message_handler(ms)


				except TimeoutError as e:
					continue
			
				except OSError as e:
					self.connection.pop()

	def message_handler(self, mes):
		pass
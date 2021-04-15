import socket
from datetime import datetime
from time import sleep
from sys import argv


host = argv[1]
port = int(argv[2])

print(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
while True:
	time = datetime.now()
	sock.sendall(str.encode('...........1234567890!@#$%&*()'))

	data = sock.recv(1024)

	print(data.decode())
	tmrv = datetime.now()
	print(f't = {(tmrv - time).seconds} {(tmrv - time).microseconds}\n')
	sleep(1)
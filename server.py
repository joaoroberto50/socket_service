import socket
import threading
from sys import argv


def run_sock(conn):
	while True:
		data = conn.recv(1024)
		if not data:
			print("Cliente Desconectado")
			conn.close()
			break
		print('.')
		conn.sendall(data)


host = ''
port = int(argv[1])

print(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))

conns = set()
sock.listen(5)
print('...')
while True:
	conn, end = sock.accept()
	print("Novo Cliente Conectado")
	conns.add(conn)
	threading.Thread(target=run_sock, args=(conn,)).start()

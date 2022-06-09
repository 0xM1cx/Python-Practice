import socket, threading

# Initialize socket 
host = "127.0.0.1"
port = 4573

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()
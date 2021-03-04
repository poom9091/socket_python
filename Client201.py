import socket
HOST = 'localhost'
PORT = 8080
s   = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
name = input("Enter your name : ")
s.sendto(name.encode(),(HOST,PORT))
while True:
    msg = input(">>")
    s.sendto(msg.encode(),(HOST,PORT))
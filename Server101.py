import socket
HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(5)
print("Server Start")
socket , address = s.accept()
while True :
    msg = socket.recv(1024)
    print(msg.decode("utf-8"))
    if msg.decode("utf-8") == 'Bye' :
        socket.close()
        break
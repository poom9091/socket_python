import socket
HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    s.connect((HOST,PORT))
    print("Server Login")
    while True:
        msg = input(">>")
        s.send(str.encode(msg))
        if(msg == 'Bye') : 
            s.close()
            break
except:
    print("Disconnect")
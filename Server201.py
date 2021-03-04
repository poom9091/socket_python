import socket
HOST = 'localhost'
PORT = 8080
s   = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
LIST={}
s.bind((HOST,PORT))
print("Server Start")
while True :
    data,add = s.recvfrom(1024)
    if add not in LIST.keys():
        LIST[add]=data.decode('utf-8')
        print (LIST[add]+"  Login")
    else :
        print(LIST[add]+" :: "+data.decode('utf-8'))
        for user in LIST.keys() :
            if add != user  :
                s.sendto(data,user)

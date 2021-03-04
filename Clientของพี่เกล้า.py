import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

uname = input("Enter user name::") #ใช้เก็บชื่อ

ip = input('Enter the IP Address::') #ใช้ login

s.connect((ip, port))
s.send(uname.encode('ascii'))

clientRunning = True
############รับผิดชอบในการรับข้อมูล####################################
def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode('ascii')
            print(msg)
        except: #ถ้าServer Down
            print('Server is Down. You are now Disconnected. Press enter to exit...')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
###################################################################


############รับผิดชอบในการส่งข้อมูล####################################
while clientRunning: #รับข้อมูลเรื่อยจนกว่าจะได้รับ **quit
    tempMsg = input()
    msg = uname + '>>' + tempMsg
    if '**quit' in msg:
        clientRunning = False
        s.send('**quit'.encode('ascii'))
    else:
        s.send(msg.encode('ascii'))
##################################################################
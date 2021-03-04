import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
serverRunning = True #ใช้ออก loop ของ serverRunning เมื่อต้องการให้ออกจาก Server
ip = str(socket.gethostbyname(socket.gethostname())) #get ip ของเครื่องตัวเอง
port = 1234

clients = {} #key เก็บ User   Values เก็บ 
s.bind((ip, port))
s.listen()
print('Server Ready...')
print('Ip Address of the Server::%s'%ip) #แสดง IP ของตัวเอง


##Thread แยกการทำงานของ client##
def handleClient(client, uname):
    clientConnected = True #ถ้ามี client เชื่อมต่อเข้ามา
    keys = clients.keys() # keys เก็บ ชื่อของ User 
    help = 'There are four commands in Messenger\n1::**chatlist=>gives you the list of the people currently online\n2::**quit=>To end your session\n3::**broadcast=>To broadcast your message to each and every person currently present online\n4::Add the name of the person at the end of your message preceded by ** to send it to particular person'
    while clientConnected: #ถ้ามี client เชื่อมต่อเข้ามา
        try:
            msg = client.recv(1024).decode('ascii') #ข้อความจะถูกเก็บไว้ใน msg
            response = 'Number of People Online\n'
            found = False
            #######   ตรวจสอบข้อความจาก msg  #######
            if '**chatlist' in msg: ###ถ้าข้อความมีคำว่า **chatlist
                clientNo = 0 #เอาไว้นับจำนวน User
                for name in keys: # Loop แสดงชื่อทั้งหมด (Client) 
                    clientNo += 1
                    response = response + str(clientNo) +'::' + name+'\n'#รวม String ทั้งหมด
                client.send(response.encode('ascii'))#ส่งข้อมูลให้ Client ที่ร้องขอ

            elif '**help' in msg: ###ถ้าข้อความมีคำว่า **help
                client.send(help.encode('ascii'))#ส่งข้อมูลให้ Client ที่ร้องขอ


            elif '**broadcast' in msg: ###ถ้าข้อความมีคำว่า **broadcast 
                msg = msg.replace('**broadcast','') ###เป็นการแทนที่ str จาก **broadcast เป็น ''
                for k,v in clients.items():  # k เก็บ user และ v เก็บ Connection 
                    v.send(msg.encode('ascii')) #ส่งให้ทุก client

            elif '**quit' in msg: ###ถ้าข้อความมีคำว่า **quit
                response = 'Stopping Session and exiting...'
                client.send(response.encode('ascii'))
                clients.pop(uname) #ลบ user ออกจาก dic
                print(uname + ' has been logged out')
                clientConnected = False #ออกจาก loop clientConnected

            else:
                for name in keys: #loop จนกว่าจะหา User ใน dic เจอ
                    if('**'+name) in msg: #ถ้า loop แล้วหา user เจอ
                        msg = msg.replace('**'+name, '') #แทนที่ str จาก **name เป็น ''
                        clients.get(name).send(msg.encode('ascii'))#ดึง Connection ที่ตรงกับ user แล้วส่งข้อมูลผ่าน Connection นั้น
                        found = True
                if(not found): #ถ้าหา User ไม่เจอ
                    client.send('Trying to send message to invalid person.'.encode('ascii'))

        except: #ถ้า client ปิด
            clients.pop(uname) #ลบ user ออกจาก dic
            print(uname + ' has been logged out')
            clientConnected = False#ออกจาก loop clientConnected



while serverRunning:
    client, address = s.accept() # client เก็บ Connection,address เก็บ Address
    print(client) 
    uname = client.recv(1024).decode('ascii')#แปลข้อมูลเป็นชื่อ User จากการข้อมูลแรกที่ Client ส่งเข้ามา
    print('%s connected to the server'%str(uname))
    client.send('Welcome to Messenger. Type **help to know all the commands'.encode('ascii'))
    if(client not in clients):#ถ้าไม่มีข้อมูล Connection ใน Dic
        clients[uname] = client #เพิ่มข้อมูลลง dic
        threading.Thread(target = handleClient, args = (client, uname)).start()
'''
Developed by Abhijith Boppe - linkedin.com/in/abhijith-boppe/
'''
from mqttSocket import IOTSocketServer, IOTSocketServerSSL, IOTSocket
import time
from clrprint import *
import datetime
import numpy as np


host = "127.0.0.1"
port = 9000

# give certificate path and key path
certfile_path = "/user/cert.pem"
keyfile_path = "/user/cert.key"
delimiter = '\r\n#*\r\n'

# give some insecure data te be filtered and sanitized to ''
lst_of_data_to_remove = [delimiter]
prev_call = 0

# this function will be called recursively to check if server want to push any data
def from_server_to_client():
    '''
    create a FIFO named pipe, make your backend application like PHP
    to write into it and you return a list. Like: ['id1 data1', 'id2 data2', 'id3 data3', .....]

    Ex: ['23234 ON SWITCH 1','23235 OFF LIGHT','232365 GET ALL SENSOR VALUES']
    (id must be numeric values only)
    
    '''
    return []

class handleEachClientHere(IOTSocket):
    clients= []
    addrs= []
    temp_addrs=[]
    numConnected= 0
    tranTask= False
    revNum= 0
    date= 'no date'
    preAddress= ''
    index=[]
    
    
    def DeviceVerify(self, id_, key):          # 'id_' - int , 'key' - string
        print("client", id_, "已線上訂閱")
        
        if "client"+str(id_) not in self.clients:
            self.clients.append("client"+str(id_))
            self.addrs.append(str(self.address))
            
        print("訂閱名單: ", self.clients)
        self.numConnected= len(self.clients)
        print("目前共"+ str(self.numConnected) + "人連線")

        '''
        This method is called when a new client is connected.
        Verify whether device id and key matches in database records
        and check if it is activated.
        (Check from DB)
        '''        
        return 1    #return True if verified successfully else false

    def handleMessage(self, id_, data):
        '''
        handle client id and data for further processing.
        create a fifo named pipe and pass the data to your
        backed application
        (make sure u remove delimeters and other vulnerable strings which effect the backend application)
        '''
        for i in lst_of_data_to_remove:         # remove delimiters/data, if any are present in client data to prevent clashes
            data.replace(i, '')
            
        if str(id_)== str(1):
            clrprint("[client"+str(id_)+"]: ", data,clr='g')
        else:
            clrprint("[client"+str(id_)+"]: ", data,clr='b')
        

        message= "hi client"+ str(id_)
        
        
        self.date= datetime.datetime.now()
        
        serverMessage= str(self.date)+ str('[localhost] say: ')+ message

        self.client.sendall(serverMessage.encode())

    def handleClose(self, error_repo=''):
        client= str(error_repo)
        client= client.split(" ")
        client_num= client[len(client)-1]
        
        print(str(datetime.datetime.now())+ " client"+str(client_num)+ " 已退出訂閱")
        
        keyword= client_num
        
        tempList= self.clients
        for i in tempList:
            if i.find(keyword.lower()) != -1:
                tempList.remove(i)
        print(tempList)
        
        self.clients= tempList
        
        keyword= str(self.address)

        self.numConnected= len(self.addrs)
        
        print("目前共"+ str(len(self.clients)) + "人連線")

        

        
        '''
        handle error if any during socket handling
        error start with "ERROR: "
        and normal socket close will end with normal message
        '''
        self.temp_addrs= self.addrs.copy()
        if "ERROR:" in str(error_repo):
            clrprint(error_repo,clr='r')
        else:
            pass

clrprint(f"Server started listening on socket {host}:{port}", clr='g')
server = IOTSocketServer(host, port, from_server_to_client,handleEachClientHere)        # without ssl
# server = IOTSocketServerSSL(host, port, from_server_to_client, handleEachClientHere, certfile = certfile_path, keyfile = keyfile_path)
server.serveforever()

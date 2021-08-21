'''
Developed by Abhijith Boppe - linkedin.com/in/abhijith-boppe/

client example for raspberry 
'''

from mqttSocket import IOTSocketClient as sock
import time
from clrprint import *

host = '127.0.0.1'
port = 9000
device_id = '0000000002'
device_key ='sica'
certfile_path = "/user/cert.pem"      # for key pinning (certificate pinning)
prev_call = 0

def someThingtoSend():
    '''
    this function is called recursively.
    read data from sensor and return data
    '''
    global prev_call
    time_now = time.time()
    if (abs(time_now - prev_call) > 1) or prev_call == 0: # send sensor data every 10 seconds
        example = 'hi Server my name is client2'
        prev_call = time_now
        return example
    else:
        return ''

def handleCmdsFromServer(data):
    '''
    This function is called when ever there is 
    data/command from the server.
    '''
    clrprint(data,clr='b')

while 1: # reconnect if socket is closed
    try:
        clrprint(f"\nEstablishing socket connection to {host}:{port}",clr='y')
        Sock= sock.connectionSet(host,port,device_id,device_key,Encrypt=False, cert_path= certfile_path)  # set IOT Socket connection with valid Device ID and Key.
        # Continiously check for receiving / tansmiting of data
        clrprint(f"Connection established successfully",clr='g')
        while 1:
            data = someThingtoSend()
            if data != '':
                sock.sendData(data)     # send data to server if data is available to send
            rcv_data = sock.recvData()  # receive data from server if available
            
            #clientMessage = Sock.recv(1024)
            #print(clientMessage)

            

    except Exception as n:
        print("cc", n)
        clr = 'r' if "ERROR:" in str(n) else 'y'
        clrprint(n,clr='r')
        clrprint('closing socket',clr='y')      
        try:
            sock.sock.close()
        except:
            pass
        time.sleep(1)
        


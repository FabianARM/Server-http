
import socket
from _thread import *
import threading 
import os
from datetime import datetime
import mimetypes

'''
if (hola = "Hola+mundo".replace("+", " ")) == "perro":
    pass
print (hola)
#print (mimetypes.guess_type("index.html"))
'''

tupla = "hola", "adios"

print (type(tupla))
yeyeyeye = "variable=hola&oculto="
ye = yeyeyeye.split("&") #division de parametros 
for element in ye :
    tupla += (element.split("=")[1], )
print(tupla)





'''
HOST,PORT = '127.0.0.1',8080

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind((HOST,PORT))
my_socket.listen(1)
my_lock = threading.Lock()
connection,address = my_socket.accept()
'''
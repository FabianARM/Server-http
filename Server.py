#Para probar el HEAD: curl --head http://localhost:8080/index.html
#Para probar el GET con Query Params: curl -i http://localhost:8080/index.html?valGet=Hola+Mundo
#Para probar el GET sin Query Params: curl -i http://localhost:8080/index.html
#Para probar el POST: curl -i -X POST -d "valPost=Hola+Mundo" http://localhost:8080/index.html
#Para probar el código 406: curl -i -H "Accept: image/gif" http://localhost/index.html

import socket
from _thread import *
import threading 
import os
from datetime import datetime
from RequestHead import RequestHead 
#aqui podemos configurar el socket para recibir peticiones.
class Servidor: 
    HOST = '127.0.0.1'
    PORT = 8080
    running = True
    #Iniciamos el socket. 
    def __init__(self):
        my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        my_socket.bind((HOST,PORT))
        my_socket.listen(1)

    def run(self): 
        connection,address = my_socket.accept()
        request, address = self.receiveResquest()
        requestSplits = request.split(' ')
        while(running)
            if self.extractMethod(requestSplits) == 'GET':
                pass # crear un hilo y ejecutar el algoritmo correspondiente
            elif self.extractMethod(requestSplits) == 'HEAD'
                pass
            elif self.extractMethod(requestSplits) == 'POST'
                pass
        







    def extractMethod(self, requestSplits):
        return requestSplits[0].strip(' ')

    #Con esto podemos recibir con exito. La operacion de recibir es bloking, por lo que lo m
    def receiveResquest(self, my_socket):
        connection,address = my_socket.accept()
        request = connection.recv(1024).decode('utf-8')
        return request, address 

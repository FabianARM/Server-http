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
from request_head_and_get import request_head_and_get 
#aqui podemos configurar el socket para recibir peticiones.
HOST = '127.0.0.1'
PORT = 8080
running = True
class Servidor: 
 
    #Iniciamos el socket. 
    def __init__(self):
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.my_socket.bind((HOST,PORT))
        self.my_socket.listen(1)
        self.request_head_get = request_head_and_get()
        self.running = True

    def extractMethod(self, requestSplits):
        return requestSplits[0].strip(' ')

    #Con esto podemos recibir con exito. La operacion de recibir es bloking, por lo que lo m
    def receiveResquest(self, my_socket, connection):
        request = connection.recv(1024).decode('utf-8')
        return request

    def run(self): 
        while self.running == True: 
            connection,address = self.my_socket.accept()
            start_new_thread(self.attend_request, (connection, ))
     
    
    def attend_request(self, connection): 
        request = self.receiveResquest(self.my_socket, connection)
        requestSplits = request.split(' ')
        if len(requestSplits) > 1:
            print(request)
            #Nota el responese ya se devuelve convertido en bytes.
            if self.extractMethod(requestSplits) == 'GET':
                header, response = self.request_head_get.execute(self.my_socket, request)
            elif self.extractMethod(requestSplits) == 'HEAD':
                pass
            elif self.extractMethod(requestSplits) == 'POST':
                pass
            final_response = header.encode('utf-8')
            final_response += response
            #print(final_response)
            connection.send(final_response)
            connection.close()

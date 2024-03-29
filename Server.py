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
from request_post import request_post
from bitacora_maker import bitacora_maker
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
        self.request_post = request_post()
        self.bitacora_maker = bitacora_maker()
        self.running = True

    def extractMethod(self, requestSplits):
        return requestSplits[0].strip(' ')

    #Con esto podemos recibir con exito. La operacion de recibir es bloking, por lo que lo m
    def receiveResquest(self, my_socket, connection):
        request = connection.recv(1024).decode('utf-8')
        return request

    def run(self): 
        file_bit = open('bitacora.csv', 'w')
        file_bit.write('Método,Estampilla derequest.split(' ') Tiempo,Servidor,Refiere,URL,Datos' + os.linesep)
        while self.running == True: 
            connection,address = self.my_socket.accept()
            start_new_thread(self.attend_request, (connection, file_bit))
     
    
    def attend_request(self, connection, bitfile): 
        request = self.receiveResquest(self.my_socket, connection)
        requestSplits = request.split(' ')
        print(request)
        if len(requestSplits) > 1:
            print(request)
            self.bitacora_maker.make_file(request,self.my_socket ,bitfile)
            #Nota el responese ya se devuelve convertido en bytes.
            if self.extractMethod(requestSplits) == 'GET' or  self.extractMethod(requestSplits) == 'HEAD':
                header, response = self.request_head_get.execute(self.my_socket, request)
            elif self.extractMethod(requestSplits) == 'POST':
                header, response = self.request_post.execute(self.my_socket, request)
            final_response = header.encode('utf-8')
            final_response += response
            #print(final_response)
            connection.send(final_response)
            connection.close()

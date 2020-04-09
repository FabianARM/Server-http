from datetime import datetime
import mimetypes
import os
from _thread import *
import threading

class request_post: 

    def execute(self, my_socket, request):
        request_split_space = request.split(" ")
        paramsPost = request_split_space[len(request_split_space)-1]
        my_file = self.extract_file_name(request_split_space)
        accept_value = mimetypes.guess_type(my_file)

        # print('paramPost-->', paramsPost[paramsPost.rfind('valPost='):])
        message = ''
        index = paramsPost.rfind('variable') #Intento agarrar el parametro. 
        message = paramsPost[index:].split('&')
        message = message[0].replace('variable=',"")
        response = '<html><body><center><h4>' + message + '</h4></center></body></html>'
        response = response.encode('utf-8')
        header = self.headers_response(my_socket, my_file, accept_value)
        return header, response

    def headers_response(self,my_socket ,requesting_file, accept_value): 
        PORT = 8080
        header = 'HTTP/1.1 200 OK\n'
        header += 'Date: ' + str(datetime.now()) + '\n'
        header += 'Host: ' + str(my_socket.getsockname()[0]) + ':' + str(PORT) + '\n'
        header += 'Server: --->Servidor 100%RealHLMBB<---\n'
        header += 'Referer: ' + str(my_socket.getsockname()[0]) + ':' + str(PORT) + '\n'
        print("Este es el nombre del archivo ", requesting_file, "Y este es el mymetype ", accept_value, "-------------------------------------------------------------------")
        header += 'Content-Length: ' + str(os.path.getsize( str(os.getcwd()) +"/"+str(requesting_file))) + ' bytes\n'
        header += 'Content-Type: ' + str(accept_value)+'\n\n'
        return header  

    def search_file(self, request): 
        my_file = request.lstrip('/') # La variable my file contiene el archivo que se esta pidiendo esto se encuentra en la primera linea de la request.
        if(my_file == ''):
            my_file = "index.html"
        file_name = open(my_file,'rb') 
        response = file_name.read()
        file_name.close()
        print(request)
        return response

    def extract_file_name(self, request_split):
        if request_split[1].find("?") != -1:
            arguments = request_split[1].split("?")#Esto es cuando viene con un paramtro
            file_name = arguments[0].replace("/", "")
        else: 
            file_name = request_split[1].replace("/", "")
        return file_name
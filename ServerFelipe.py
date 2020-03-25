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
 
HOST,PORT = '127.0.0.1',8080

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
my_socket.bind((HOST,PORT))
my_socket.listen(1)
my_lock = threading.Lock()

file = open('bitacora.csv', 'w')
file.write('Método,Estampilla derequest.split(' ') Tiempo,Servidor,Refiere,URL,Datos' + os.linesep)
bitacoraLine = ''

def getServerResponseHeaders(myfile, requesting_file):
    header = 'HTTP/1.1 200 OK\n'
    header += 'Date: ' + str(datetime.now()) + '\n'
    bitLine = str(datetime.now()) + ',' #Estampilla de tiempo en bitácora
    
    header += 'Host: ' + str(my_socket.getsockname()[0]) + ':' + str(PORT) + '\n'
    bitLine += str(my_socket.getsockname()[0]) + ':' + str(PORT) + ',' #Servidor en bitácora
   
    header += 'Server: --->Servidor AK7<---\n'
    header += 'Referer: ' + str(my_socket.getsockname()[0]) + ':' + str(PORT) + '\n'
    bitLine += str(my_socket.getsockname()[0]) + ':' + str(PORT) + ',' #Referente en bitácora ######################################
    bitLine += requesting_file + ',' #URL en bitácora
    
    folderRoot = os.getcwd()
    header += 'Content-Length: ' + str(os.path.getsize(folderRoot + str(requesting_file))) + ' bytes\n'
    
    if(myfile.endswith(".png")):
        mimetype = 'image/png'
    elif(myfile.endswith(".css")):
        mimetype = 'text/css'
    else:
        mimetype = 'text/html'
    header += 'Content-Type: ' + str(mimetype)+'\n\n'

    return [header,bitLine]


def threaded(my_socket, connection, fileAux):   
    request = connection.recv(1024).decode('utf-8')
    string_list = request.split(' ')  # Quita espacios del request
    
    if len(string_list) > 1:  #Para evitar error que pasado un rato el server se cae
        method = string_list[0]
        requesting_file = string_list[1]
    
        print('-------------------------------Request:-------------------------------')
        print(request)
        print('----------------------------------------------------------------------')
        bitacoraLine = ''
        bitacoraLine = method + ',' #Agregamos método a bitácora
        # file.write(bitacoraLine) 
        myfile = ''
        queryString = False
        acceptHedersRecv = False
        if requesting_file.find("?") == -1:    # No hay query string para GET
            myfile = requesting_file.split('?')[0] 
        else:                                   # Si hay query string y hay que procesarlo
            queryString = True
            myQueryString = requesting_file.split('?')[1]
            parametersArray = myQueryString.split('&')

        #Carga el index como default        
        myfile = myfile.lstrip('/') # La variable my file contiene el archivo que se esta pidiendo esto se encuentra en la primera linea de la request.
        if(myfile == ''):
            requesting_file = '/index.html' 
            myfile = 'index.html'    
        
        if method.strip(' ') == 'GET' or method.strip(' ') == 'HEAD': # GET y HEAD son casi lo mismo solo que HEAD solo devuelve headers
            try:
                if request.find('Accept:') != -1: #Si encuentra el accept entra. 
                    reqFileSplitted = requesting_file.split('.')
                    AcceptValue = ''
                    if reqFileSplitted[1] != 'png': #Si no es png es textyo ? 
                        AcceptValue = 'text/'+ reqFileSplitted[1]
                    else:
                        AcceptValue = 'image/'+ reqFileSplitted[1]
                    
                    stringAccept = request.split('Accept: ')
                    stringAccept = stringAccept[1].split('\r\n\r\n')
                    
                    if stringAccept[0] != '/' and stringAccept[0].find(AcceptValue) == -1 :#Error 406. Si viene algun / y no tienen accepted value
                        acceptHedersRecv = True
                        bitacoraLine = ''
                        header = 'HTTP/1.1 406 Not Acceptable\n\n'
                        response = '<html><body><center><h3>Error 406: File not Acceptable</h3><p>Servidor AK7</p></center></body></html>'.encode('utf-8')

                if queryString: # Procesamos un query string desde su URL, esto para el GET
                    
                    message = ''
                    for parameter in parametersArray:
                        index = parameter.find('=')
                        parameter = parameter[index + 1 :]
                        auxList =  parameter.split('+') # En *auxlist* quedan los parametros. 
                    #Aqui lo que hace es volver a unir el mensaje, podemos investigar un replace.
                    for element in auxList:
                        message = message  +  element + ' '
                    response = '<html><body><center><h4>' + message + '</h4></center></body></html>'
                    response = response.encode('utf-8')
                    #Para este punto ya hay una respuesta creada junto con el mensaje que se desea.
                else: # GET sin query strings
                    if not acceptHedersRecv:
                        file = open(myfile,'rb') 
                        response = file.read()
                        file.close()
                
                if not acceptHedersRecv:
                    lista = getServerResponseHeaders(myfile, requesting_file)
                    header = lista[0]
                    bitacoraLine += lista[1]
                    if queryString:
                        bitacoraLine += myQueryString + os.linesep  #Agregamos datos a bitácora
                    else:
                        bitacoraLine += ' ' + os.linesep

            except Exception as e:
                bitacoraLine = ''
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = '<html><body><center><h3>Error 404: File not found</h3><p>Servidor AK7</p></center></body></html>'.encode('utf-8')
        #aqui termina el get y head. 
        elif method.strip(' ') == 'POST':
            paramsPost = string_list[len(string_list)-1]
            # print('paramPost-->', paramsPost[paramsPost.rfind('valPost='):])
            message = ''
            index = paramsPost.rfind('=') #Intento agarrar el parametro. 
            auxString = paramsPost[index + 1 :]
            auxList =  auxString.split('+')
            for element in auxList:
                message = message  +  element + ' '

            response = '<html><body><center><h4>' + message + '</h4></center></body></html>'
            response = response.encode('utf-8')
 
            lista = getServerResponseHeaders(myfile, requesting_file)
            header = lista[0]
            bitacoraLine += lista[1]
            bitacoraLine += paramsPost[paramsPost.rfind('valPost='):] + os.linesep

        else:
            bitacoraLine = ''
            header = 'HTTP/1.1 501 Not implemented\n\n'
            response = '<html><body><center><h3>Error 501: Method not implemented</h3><p>Servidor AK7</p></center></body></html>'.encode('utf-8')
    
        final_response = header.encode('utf-8')
        final_response += response
        connection.send(final_response)
        connection.close()
        if bitacoraLine != '':
            fileAux.write(bitacoraLine)
        # bitacoraLine = ''
      

def main():
    print('Ip HOST ', HOST) 
    print('Serving on port ',PORT)
    while True: 
        connection,address = my_socket.accept()
        start_new_thread(threaded, (my_socket,connection, file))



main()
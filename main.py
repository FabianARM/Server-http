from Server import Servidor
import os 

print (os.path.abspath(os.getcwd()))
try:
    archivo = open("index.html", 'rb')
except Exception as identifier:
    print(identifier)
    
server = Servidor()

server.run()
''''
b'HTTP/1.1 406 Not Acceptable\n\n<html><body><center><h3>Error 406: File not Acceptable</h3><p>Servidor AK7</p></center></body></html>'
b'HTTP/1.1 404 Not Found\n\n<html><body><center><h3>Error 404: File not found</h3><p>Servidor AK7</p></center></body></html>'

'''
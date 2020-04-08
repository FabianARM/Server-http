
import platform
import socket
from _thread import *
import threading 
import os
from datetime import datetime

import mimetypes




print(mimetypes.guess_type("style.css"))

print(platform.system())


archivo = open("index.html", 'rb')

print("Esto esta funcando bien", archivo)

print (os.path.dirname(os.path.abspath("index.html")))   

''''if platform.system() == "Windows":
    file = open("TareaServer/" + myfile,'rb') 
    response = file.read()
    file.close()
else:'''
from datetime import datetime
import os 
class bitacora_maker: 

    def extract_method(self, requestSplits):
        return requestSplits[0].strip(' ')

    def make_timestamp(self):
        return str(datetime.now())

    def get_server_name(self, my_socket):
        return str(my_socket.getsockname()[0])

    def extract_url(self, request_split): 
        return request_split[1]
    
    def extract_param_post(self, request_split):
        return  request_split[len(request_split)-1]

    def make_file(self, request, my_socket, bitacora_file): 
        request_split = request.split(" ")
        method = self.extract_method(request_split)
        timestamp = self.make_timestamp()
        server = self.get_server_name(my_socket)
        referer = '' 
        URL = self.extract_url(request_split)
        if(method == 'POST'):
            data = self.extract_param_post(request_split)
        else:
            data = "" 

        bitacora_line = method + ", " + timestamp + ", " + server + ", " + referer + ", " + URL + ", " + data + os.linesep
        bitacora_file.write(bitacora_line)
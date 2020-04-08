

class RequestPost: 
    

    def execute(self, request):
        request_split = request.split(" ")
        paramPost = request_split[len(request_split) - 1]
        
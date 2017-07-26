from Commons.Constants import TCP_MESSAGE


class Communicator:
    def __init__(self, ip, port):
        self.Server_Ip = ip
        self.Server_Port = int(port)

    def sendDataRequest(self):
        print("Sending Data Request to " + self.Server_Ip + " on Port " + str(self.Server_Port))
        import socket
        # server = 'pythonprogramming.net'
        result = ""
        # port = 80
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(s)
        server_ip = socket.gethostbyname(self.Server_Ip)
        print(server_ip)
        request = TCP_MESSAGE
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Sending TCP request '" + TCP_MESSAGE + "' and Waiting for Response...")
            s.connect((self.Server_Ip, self.Server_Port))
            s.send(request.encode())
            result = s.recv(4096)
            print(result)
        except socket.error:
            print("Socket Error Exception Thrown!")
        return result

    def setupConnection(self, server_ip, server_port):
        self.Server_Ip = server_ip
        self.Server_Port = server_port
        pass

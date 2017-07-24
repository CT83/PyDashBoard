class Communicator:
    def __init__(self):
        self.Server_Ip = ""
        self.Server_Port = 0

    def sendDataRequest(self):
        print("Sending Data Request to " + self.Server_Ip + " on Port " + str(self.Server_Port))
        import socket
        server = 'pythonprogramming.net'

        port = 80
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(s)
        server_ip = socket.gethostbyname(server)
        print(server_ip)
        request = "GET / HTTP/1.1\nHost: " + server + "\n\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("pythonprogramming.net", 80))
        s.send(request.encode())
        result = s.recv(4096)

        print(result)
        pass

    def setupConnection(self, server_ip, server_port):
        self.Server_Ip = server_ip
        self.Server_Port = server_port
        pass


def doStuff(self):
    self.top_PoleTest_T2[0][0].setText("Set by thread")
    for i in range(100000000):
        print i

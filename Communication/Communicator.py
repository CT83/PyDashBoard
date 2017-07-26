import socket

from Commons.Constants import TCP_MESSAGE


class Communicator:
    def __init__(self, ip, port):
        self.Server_Ip = ip
        self.port = int(port)

    def sendDataRequest(self):
        print("Sending Data Request to " + self.Server_Ip + " on Port " + str(self.port))
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
            s.connect((self.Server_Ip, self.port))
            s.send(request.encode())
            result = s.recv(4096)
            print(result)
        except socket.error:
            print("Socket Error Exception Thrown!")
        print("Request Sent")
        return result

    def startServer(self):
        print("Started Threaded Server")
        TCP_IP = ''
        TCP_PORT = 5005
        BUFFER_SIZE = 4024  # Normally 4024, but we want fast response

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        conn, addr = s.accept()
        print 'Connection address:', addr
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print "Received data:", data
            conn.sendall(data)  # echo
        conn.close()
        print("Server Closed")

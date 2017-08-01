import socket
import threading

from Commons.Constants import TCP_MESSAGE


class Communicator:
    def __init__(self, ip, port):
        self.Server_Ip = ip
        self.port = int(port)

    def sendDataRequest(self):
        print("Sending Data Request to " + self.Server_Ip + " on Port " + str(self.port))
        print("Network Thread Name:" + threading.current_thread().name)
        import socket
        result = ""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_ip = socket.gethostbyname(self.Server_Ip)
        request = TCP_MESSAGE
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.Server_Ip, self.port))
            s.send(request.encode())
            result = s.recv(4096)
        except socket.error:
            print("Socket Error Exception Thrown!")
        print ("Done!")
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

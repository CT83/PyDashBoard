import ConfigParser

SERVER_IP = ""
SERVER_PORT = ""


def import_settings(file_name):
    print("Loading Settings...")
    config = ConfigParser.ConfigParser()
    config.read(file_name)
    server_ip = config.get('Server_Info', 'server_ip')
    server_port = config.get('Server_Info', 'server_port')
    global SERVER_IP
    global SERVER_PORT
    SERVER_IP = server_ip
    SERVER_PORT = server_port

import time

from PySide import QtGui

from Communication.Communicator import Communicator
from Communication.Parser import parse_and_write_to_vars
from Settings import Settings
from Settings.Settings import *


def initiateBackgroundTasks(ui):
    import_settings("Settings.ct83")
    print("Server IP  :" + Settings.SERVER_IP)
    print("Server Port:" + Settings.SERVER_PORT)
    # commServer = Communicator(Settings.SERVER_IP, Settings.SERVER_PORT)
    # s = Thread(target=Communicator.startServer, args=(commServer,))
    # s.daemon = True
    # s.start()

    while 1:
        commClient = Communicator(Settings.SERVER_IP, Settings.CLIENT_PORT)
        response = commClient.sendDataRequest()
        parse_and_write_to_vars(ui, response)
        QtGui.QApplication.processEvents()
        time.sleep(1)

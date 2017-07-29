import time

from Communication.Communicator import Communicator
from Communication.Parser import parse_and_write_to_vars
from GUI.MainWindowUI import UIMainWindow
from Settings import Settings
from Settings.Settings import *


def initiateBackgroundTasks(ui):
    import_settings("Settings.ct83")
    print("Server IP  :" + Settings.SERVER_IP)
    print("Server Port:" + Settings.SERVER_PORT)

    ui.top_PoleTest_T2[0][0].setText("Set by thread")
    ui.top_PoleTest_T2[0][2].setText("Set by thread")

    # commServer = Communicator(Settings.SERVER_IP, Settings.SERVER_PORT)
    # s = Thread(target=Communicator.startServer, args=(commServer,))
    # s.daemon = True
    # s.start()

    commClient = Communicator(Settings.SERVER_IP, Settings.CLIENT_PORT)
    response = commClient.sendDataRequest()
    while 1:
        parse_and_write_to_vars(ui, response)
        UIMainWindow.self.processEvents()
        time.sleep(1)

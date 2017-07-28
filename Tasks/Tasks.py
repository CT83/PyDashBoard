from Communication.Communicator import Communicator
from Communication.Parser import parse_and_write_to_vars
from Settings import Settings
from Settings.Settings import *


def initiateBackgroundTasks(self):
    import_settings("Settings.ct83")
    print("Server IP  :" + Settings.SERVER_IP)
    print("Server Port:" + Settings.SERVER_PORT)

    self.top_PoleTest_T2[0][0].setText("Set by thread")
    self.top_PoleTest_T2[0][2].setText("Set by thread")

    # commServer = Communicator(Settings.SERVER_IP, Settings.SERVER_PORT)
    # s = Thread(target=Communicator.startServer, args=(commServer,))
    # s.daemon = True
    # s.start()

    commClient = Communicator(Settings.SERVER_IP, Settings.CLIENT_PORT)
    response = commClient.sendDataRequest()
    parse_and_write_to_vars(response)

import time
from threading import current_thread

from PySide import QtCore
from PySide import QtGui

from Communication.Communicator import Communicator
from Communication.Parser import parse_and_write_to_vars
from Settings import Settings
from Settings.Settings import *


class InvokeEvent(QtCore.QEvent):
    EVENT_TYPE = QtCore.QEvent.Type(QtCore.QEvent.registerEventType())

    def __init__(self, fn, *args, **kwargs):
        QtCore.QEvent.__init__(self, InvokeEvent.EVENT_TYPE)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs


class Invoker(QtCore.QObject):
    def event(self, event):
        event.fn(*event.args, **event.kwargs)
        print (current_thread().name)
        return True


_invoker = Invoker()


def invoke_in_main_thread(fn, *args, **kwargs):
    QtCore.QCoreApplication.postEvent(_invoker,
                                      InvokeEvent(fn, *args, **kwargs))



def initiateBackgroundTasks(ui):
    import_settings("Settings.ct83")
    print("Server IP  :" + Settings.SERVER_IP)
    print("Server Port:" + Settings.SERVER_PORT)
    # commServer = Communicator(Settings.SERVER_IP, Settings.SERVER_PORT)
    # s = Thread(target=Communicator.startServer, args=(commServer,))
    # s.daemon = True
    # s.start()

    # while 1:
    commClient = Communicator(Settings.SERVER_IP, Settings.CLIENT_PORT)
    response = commClient.sendDataRequest()
    parse_and_write_to_vars(ui, response)
    QtGui.QApplication.processEvents()
    time.sleep(1)

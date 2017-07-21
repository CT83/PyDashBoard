import sys

from PySide import QtGui

from CommonMethods.CommonMethods import display
from GUI.MainWindowUI import Ui_MainWindow

ui = Ui_MainWindow()
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui.setupUi(MainWindow)


def generate_new_test(test_self):
    print ("Adding Tests:" + test_self.test_name)
    ui.addNewTest(test_self.test_name)
    MainWindow.show()


def generate_poles(test_self):
    display("Generating Poles respectively for:" + test_self.pole_list_list)
    ui.addNewPole(test_self)
    MainWindow.show()


def drawMainWindow():
    print ("Drawing MainWindow")
    # createEmptyMainWindow()
    createGUI()


def createGUI():
    MainWindow.show()
    sys.exit(app.exec_())

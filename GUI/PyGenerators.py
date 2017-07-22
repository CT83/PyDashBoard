import sys

from GUI.MainWindowUI import Ui_MainWindow
from PySide import QtGui

from Commons.Methods import display

ui = Ui_MainWindow()
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui.setupUi(MainWindow)


def generate_new_test(test_self):
    print ("Adding Tests:" + test_self.test_name)
    ui.addNewTest(test_self.test_name)
    MainWindow.show()


def generate_poles(test_self, index):
    display("Generating Poles respectively for:" + str(test_self.pole_list_list))
    ui.addNewPole(test_self, index)
    MainWindow.show()


def drawMainWindow():
    print ("Drawing MainWindow")
    # createEmptyMainWindow()
    createGUI()


def createGUI():
    MainWindow.show()
    sys.exit(app.exec_())

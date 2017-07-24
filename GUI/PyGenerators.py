import sys

from PySide import QtGui

from Commons.Methods import display
from GUI.MainWindowUI import UIMainWindow

ui = UIMainWindow()
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui.setupUi(MainWindow)
ui.definitions()
display("Setting up Main Window")


def generate_new_test(test_self):
    print ("Adding Tests:" + test_self.test_name)
    ui.addNewTest(test_self)
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
    app.exec_()

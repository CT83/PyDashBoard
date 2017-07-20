import sys

from PySide import QtGui

from GUI.MainWindowUI import Ui_MainWindow

ui = Ui_MainWindow()
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui.setupUi(MainWindow)


def generateNewTest(test_name):
    print ("Adding Tests:" + test_name)
    ui.addNewTest(test_name)
    MainWindow.show()



def drawMainWindow():
    print ("Drawing MainWindow")
    # createEmptyMainWindow()
    createGUI()


def createGUI():
    # ui.addNewTest()
    generateNewTest("Ground Test")
    generateNewTest("Trip Test")

    MainWindow.show()
    sys.exit(app.exec_())

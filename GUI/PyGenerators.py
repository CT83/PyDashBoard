from Commons.Methods import display
from GUI.MainWindowUI import ui, MainWindow


def generate_new_test(test_self):
    print ("Adding Tests:" + test_self.test_name)
    ui.addNewTest(test_self)
    MainWindow.show()


def generate_poles(test_self, index):
    display("Generating Poles respectively for:")
    ui.addNewPole(test_self, index)
    MainWindow.show()


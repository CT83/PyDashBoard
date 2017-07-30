from PySide import QtCore, QtGui

from Commons.Constants import MAX_SIZE
from Commons.Methods import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

testIndex = 0
test_ctr = 0
pole_ctr = 0
val_ctr = 0


class UIMainWindow(object):
    def definitions(self):
        self.top_PoleTestLegend = [[QtGui.QLabel(self.centralwidget) for i in range(MAX_SIZE - 2)] for j in
                                   range(MAX_SIZE)]
        self.top_PoleTest_T1 = [[QtGui.QLabel(self.centralwidget) for i in range(MAX_SIZE - 2)] for j in
                                range(MAX_SIZE)]
        self.top_PoleTest_T0 = [[QtGui.QLabel(self.centralwidget) for i in range(MAX_SIZE - 2)] for j in
                                range(MAX_SIZE)]
        self.top_PoleTest_T2 = [[QtGui.QLabel(self.centralwidget) for i in range(MAX_SIZE - 2)] for j in
                                range(MAX_SIZE)]

    def addNewTestPole(self, test_self, test_i, pole_i):
        self.individualTestPerPole = QtGui.QVBoxLayout()
        self.individualTestPerPole.setObjectName(_fromUtf8("individualTestPerPole"))

        font = QtGui.QFont()
        font.setPointSize(11)
        print str(pole_i) + " " + str(test_i)
        self.top_PoleTestLegend[test_i][pole_i].setFont(font)
        self.top_PoleTestLegend[test_i][pole_i].setStyleSheet(_fromUtf8("QLabel {\n"
                                                                        "qproperty-alignment: AlignCenter;\n"
                                                                        "color:white;\n"
                                                                        "}\n"
                                                                        ""))
        self.top_PoleTestLegend[test_i][pole_i].setObjectName(_fromUtf8("ip_3"))
        self.individualTestPerPole.addWidget(self.top_PoleTestLegend[test_i][pole_i])

        self.top_PoleTest_T0[test_i][pole_i] = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.top_PoleTest_T0[test_i][pole_i].setFont(font)
        self.top_PoleTest_T0[test_i][pole_i].setStyleSheet(_fromUtf8("QLabel {\n"
                                                                     "qproperty-alignment: AlignCenter;\n"
                                                                     "color:white;\n"
                                                                     "}\n"
                                                                     ""))
        self.top_PoleTest_T0[test_i][pole_i].setObjectName(_fromUtf8("ip_2"))
        self.individualTestPerPole.addWidget(self.top_PoleTest_T0[test_i][pole_i])
        self.top_PoleTest_T1[test_i][pole_i] = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.top_PoleTest_T1[test_i][pole_i].setFont(font)
        self.top_PoleTest_T1[test_i][pole_i].setStyleSheet(_fromUtf8("QLabel {\n"
                                                                     "qproperty-alignment: AlignCenter;\n"
                                                                     "color:white;\n"
                                                                     "}\n"
                                                                     ""))
        self.top_PoleTest_T1[test_i][pole_i].setObjectName(_fromUtf8("ip_1"))
        self.individualTestPerPole.addWidget(self.top_PoleTest_T1[test_i][pole_i])

        self.top_PoleTest_T2[test_i][pole_i] = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.top_PoleTest_T2[test_i][pole_i].setFont(font)
        self.top_PoleTest_T2[test_i][pole_i].setStyleSheet(_fromUtf8("QLabel {\n"
                                                                     "qproperty-alignment: AlignCenter;\n"
                                                                     "color:white;\n"
                                                                     "}\n"
                                                                     ""))
        self.top_PoleTest_T2[test_i][pole_i].setObjectName(_fromUtf8("ip_0"))
        self.individualTestPerPole.addWidget(self.top_PoleTest_T2[test_i][pole_i])
        self.ip_lineBottom = QtGui.QFrame(self.centralwidget)
        self.ip_lineBottom.setStyleSheet(_fromUtf8("white"))
        self.ip_lineBottom.setFrameShape(QtGui.QFrame.HLine)
        self.ip_lineBottom.setFrameShadow(QtGui.QFrame.Sunken)
        self.ip_lineBottom.setObjectName(_fromUtf8("ip_lineBottom"))

        self.individualTestPerPole.addWidget(self.ip_lineBottom)
        self.individualTestPerPole.addWidget(self.ip_lineBottom)
        self.individualTestPerPole.addWidget(self.ip_lineBottom)
        self.TestVerticalLayout.addLayout(self.individualTestPerPole)

        self.top_PoleTestLegend[test_i][pole_i].setText(str(test_i))
        self.top_PoleTest_T0[test_i][pole_i].setText(_translate("MainWindow", "PASS", None))
        self.top_PoleTest_T0[test_i][pole_i].setStyleSheet(
            "QLabel { background-color : green; color : white; qproperty-alignment: AlignCenter;}");

        self.top_PoleTest_T1[test_i][pole_i].setText(_translate("MainWindow", "FAIL", None))
        self.top_PoleTest_T1[test_i][pole_i].setStyleSheet(
            "QLabel { background-color : red; color : white; qproperty-alignment: AlignCenter;}");
        self.top_PoleTest_T2[test_i][pole_i].setText(_translate("MainWindow", "In Progress", None))
        self.top_PoleTest_T2[test_i][pole_i].setStyleSheet(
            "QLabel { background-color : orange; color : black; qproperty-alignment: AlignCenter;}")

    def addNewPole(self, test_self, index):
        global pole_ctr
        pole_ctr = pole_ctr + 1
        self.individualPole = QtGui.QVBoxLayout()
        self.individualPole.setObjectName(_fromUtf8("individualPole"))
        self.pole_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pole_label.setFont(font)
        self.pole_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pole_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pole_label.setAutoFillBackground(True)
        self.pole_label.setObjectName(_fromUtf8("pole_label"))
        self.individualPole.addWidget(self.pole_label)
        self.pole_label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pole_label_3.setFont(font)
        self.pole_label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pole_label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pole_label_3.setAutoFillBackground(True)
        self.pole_label_3.setStyleSheet(_fromUtf8("QLabel {\n"
                                                  "qproperty-alignment: AlignCenter;\n"
                                                  "color:white;\n"
                                                  "}\n"
                                                  ""))
        self.pole_label_3.setObjectName(_fromUtf8("pole_label_3"))
        self.individualPole.addWidget(self.pole_label_3)
        self.pole_label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pole_label_2.setFont(font)
        self.pole_label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pole_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pole_label_2.setAutoFillBackground(True)
        self.pole_label_2.setStyleSheet(_fromUtf8("QLabel {\n"
                                                  "qproperty-alignment: AlignCenter;\n"
                                                  "color:white;\n"
                                                  "}\n"
                                                  ""))
        self.pole_label_2.setObjectName(_fromUtf8("pole_label_2"))
        self.individualPole.addWidget(self.pole_label_2)
        self.pole_label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pole_label_4.setFont(font)
        self.pole_label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pole_label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pole_label_4.setAutoFillBackground(True)
        self.pole_label_4.setStyleSheet(_fromUtf8("QLabel {\n"
                                                  "qproperty-alignment: AlignCenter;\n"
                                                  "color:white;\n"
                                                  "}\n"
                                                  ""))
        self.pole_label_4.setObjectName(_fromUtf8("pole_label_4"))
        self.individualPole.addWidget(self.pole_label_4)
        self.pole_line = QtGui.QFrame(self.centralwidget)
        self.pole_line.setStyleSheet(_fromUtf8("white"))
        self.pole_line.setFrameShape(QtGui.QFrame.HLine)
        self.pole_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.pole_line.setObjectName(_fromUtf8("pole_line"))
        self.individualPole.addWidget(self.pole_line)
        self.PolesVerticalLayout.addLayout(self.individualPole)

        self.pole_label_3.setStyleSheet(
            "QLabel { background-color : black; color : white; qproperty-alignment: AlignCenter;}")
        self.pole_label_2.setStyleSheet(
            "QLabel { background-color : black; color : white; qproperty-alignment: AlignCenter;}")
        self.pole_label_4.setStyleSheet(
            "QLabel { background-color : black; color : white; qproperty-alignment: AlignCenter;}")
        self.pole_label.setStyleSheet(
            "QLabel { background-color : black; color : green; qproperty-alignment: AlignCenter;}")

        self.pole_label.setText(_translate("MainWindow", "Pole_" + str(index), None))
        self.pole_label_3.setText(_translate("MainWindow", test_self.pole_list_list[index][0], None))
        self.pole_label_2.setText(_translate("MainWindow", test_self.pole_list_list[index][1], None))
        self.pole_label_4.setText(_translate("MainWindow", test_self.pole_list_list[index][2], None))

    def addNewTest(self, test_self):
        display("Calling addNewTest...")
        self.TestVerticalLayout = QtGui.QVBoxLayout()
        self.TestVerticalLayout.setSpacing(0)
        self.TestVerticalLayout.setObjectName(_fromUtf8("TestVerticalLayout"))
        self.test_nameLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_nameLabel.setFont(font)
        self.test_nameLabel.setStyleSheet(_fromUtf8("QLabel {\n"
                                                    "qproperty-alignment: AlignCenter;\n"
                                                    "color:white;\n"
                                                    "}\n"
                                                    ""))
        self.test_nameLabel.setObjectName(_fromUtf8("test_nameLabel"))

        self.ip_lineTop = QtGui.QFrame(self.centralwidget)
        self.ip_lineTop.setStyleSheet(_fromUtf8("white"))
        self.ip_lineTop.setFrameShape(QtGui.QFrame.HLine)
        self.ip_lineTop.setFrameShadow(QtGui.QFrame.Sunken)
        self.ip_lineTop.setObjectName(_fromUtf8("ip_lineTop"))
        self.TestVerticalLayout.addWidget(self.ip_lineTop)

        # Add new TestPoles Here.
        global testIndex
        for i in xrange(pole_ctr):
            self.addNewTestPole(test_self, testIndex, i)
        testIndex = testIndex + 1
        self.TestsHorizontalLayout.addLayout(self.TestVerticalLayout)
        self.setupSlot()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(843, 480)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 130))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setAnimated(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.StartButton = QtGui.QPushButton(self.centralwidget)
        self.StartButton.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.StartButton.setFont(font)
        self.StartButton.setAcceptDrops(True)
        self.StartButton.setStyleSheet(_fromUtf8("QPushButton{\n"
                                                 "    background-color:green;\n"
                                                 "    color:white;        \n"
                                                 "}"))
        self.StartButton.setFlat(False)
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.gridLayout.addWidget(self.StartButton, 1, 0, 1, 1)
        self.TestParentLayout = QtGui.QVBoxLayout()
        self.TestParentLayout.setObjectName(_fromUtf8("TestParentLayout"))
        self.TestsHorizontalLayout = QtGui.QHBoxLayout()
        self.TestsHorizontalLayout.setObjectName(_fromUtf8("TestsHorizontalLayout"))
        self.TestParentLayout.addLayout(self.TestsHorizontalLayout)
        self.gridLayout.addLayout(self.TestParentLayout, 0, 2, 1, 1)
        self.PolesVerticalLayout = QtGui.QVBoxLayout()
        self.PolesVerticalLayout.setObjectName(_fromUtf8("PolesVerticalLayout"))
        # spacerItem = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        # self.PolesVerticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.PolesVerticalLayout, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_2.setStyleSheet(_fromUtf8("white"))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)

        self.mini_log = QtGui.QTextEdit(self.centralwidget)
        self.mini_log.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mini_log.setFont(font)
        self.mini_log.setStyleSheet(_fromUtf8("QLabel {\n"
                                              "qproperty-alignment: AlignLeft;\n"
                                              "}\n"
                                              ""))
        self.mini_log.setReadOnly(True)
        self.gridLayout.addWidget(self.mini_log, 1, 2, 1, 1)
        self.mini_log.setText("Test Text")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.StartButton.setText(_translate("MainWindow", "Start", None))

    def setupSlot(self):
        downloader = UIThread()
        downloader.data_downloaded.connect(self.on_data_ready)
        downloader.run()

    def on_data_ready(self, data):
        print (data + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.top_PoleTest_T1[0][0].setText("SSSSSSSSSSS")
        self.top_PoleTest_T2[2][2].setText("SSSSSSSSSSS")
        self.top_PoleTest_T2[2][3].setStyleSheet(
            "QLabel { background-color : orange; color : black; qproperty-alignment: AlignCenter;}")


class MainWindow(QtGui.QMainWindow, UIMainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
        self.setupUi(self)


class UIThread(QtCore.QThread):
    data_downloaded = QtCore.Signal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        self.data_downloaded.emit("dataadsd")

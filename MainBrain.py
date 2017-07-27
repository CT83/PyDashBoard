from threading import Thread

from Commons.Constants import *
from Commons.Methods import display_mini
from GUI.PyGenerators import *
from Tasks.Tasks import initiateBackgroundTasks
from Test.Test import Test

display(application_name + " Initialised...")
display("Generating UI...")

magneticTest = Test(magneticTestName, magneticPoles, magneticContinuous, magneticFinalResult)
# Poles which appear on the left panel
thermalTest = Test(thermalTestName, thermalPoles, thermalContinuous, thermalFinalResult)
testTest = Test(TestTestName, TestPoles, TestContinuous, TestFinalResult)
test2Test = Test(Test2TestName, Test2Poles, Test2Continuous, Test2FinalResult)

# Add the Test with the maximum number of Poles here
for i in xrange(NUMBER_OF_POLES):
    generate_poles(thermalTest, i)

# Add new Vertical Columns for Tests
generate_new_test(thermalTest)
generate_new_test(magneticTest)
generate_new_test(testTest)
generate_new_test(test2Test)

# generate_poles(thermalTest,3)
# generate_poles(thermalTest,4)

print("Number of Poles=" + str(ui.PolesVerticalLayout.count() - ITEMS_EXCEPT_POLES))
# print("Pole"+str(ui.PolesVerticalLayout)


ui.top_PoleTestLegend[0][0].setText(thermalTest.test_name + " Test")
ui.top_PoleTestLegend[0][1].setText(magneticTest.test_name + " Test")
ui.top_PoleTestLegend[0][2].setText(testTest.test_name + " Test")
ui.top_PoleTestLegend[0][3].setText(test2Test.test_name + " Test")

# first value is x axis and second is y
ui.top_PoleTest_T0[0][0].setText("T0_00")
ui.top_PoleTest_T1[0][0].setText("T1_00")
ui.top_PoleTest_T2[0][0].setText("T2_00")

ui.top_PoleTest_T0[1][0].setText("T0_10")
ui.top_PoleTest_T1[0][1].setText("T1_01")
ui.top_PoleTest_T2[1][0].setText("T2_10")


display_mini(ui, "Starting...")
thread = Thread(target=initiateBackgroundTasks, args=(ui,))
thread.daemon = True
thread.start()

drawMainWindow()
print("Done Drawing MainWindow")

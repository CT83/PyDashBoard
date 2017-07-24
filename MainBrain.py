from BusinessLogic.Test import Test
from Commons.Constants import *
from GUI.PyGenerators import *

display(application_name + " Initialised...")
display("Generating UI...")

magneticTest = Test(magneticTestName, magneticPoles, magneticContinuous, magneticFinalResult)
# Poles which appear on the left panel
thermalTest = Test(thermalTestName, thermalPoles, thermalContinuous, thermalFinalResult)
testTest = Test(TestTestName, TestPoles, TestContinuous, TestFinalResult)
test2Test = Test(Test2TestName, Test2Poles, Test2Continuous, Test2FinalResult)

for i in xrange(NUMBER_OF_POLES):
    generate_poles(thermalTest, i)
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
ui.top_PoleTest_T0[0][0].setText("T0")
ui.top_PoleTest_T1[0][0].setText("T1")
ui.top_PoleTest_T2[0][0].setText("T2")
drawMainWindow()

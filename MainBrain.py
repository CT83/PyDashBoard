from BusinessLogic.Test import Test
from Commons.Constants import *
from GUI.PyGenerators import *

display(application_name + " Initialised...")
display("Generating UI...")

magneticTest = Test(magneticTestName, magneticPoles, magneticContinuous, magneticFinalResult)
generate_new_test(magneticTest)

thermalTest = Test(thermalTestName, thermalPoles, thermalContinuous, thermalFinalResult)
generate_new_test(thermalTest)

testTest = Test(TestTestName, TestPoles, TestContinuous,
                TestFinalResult)
generate_new_test(testTest)

test2Test = Test(Test2TestName, Test2Poles, Test2Continuous,
                 Test2FinalResult)
generate_new_test(test2Test)

# Poles which appear on the left panel
generate_poles(thermalTest, 0)
generate_poles(magneticTest, 1)
generate_poles(testTest, 2)
generate_poles(test2Test, 3)
# generate_poles(thermalTest,3)
# generate_poles(thermalTest,4)

print("Number of Poles=" + str(ui.PolesVerticalLayout.count() - ITEMS_EXCEPT_POLES))
# print("Pole"+str(ui.PolesVerticalLayout)

ui.ip_3[3][4].setText("Globally Manipulated")
drawMainWindow()

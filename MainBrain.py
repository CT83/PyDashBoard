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
generate_new_test(testTest)

generate_poles(thermalTest, 1)
generate_poles(thermalTest, 2)
# generate_poles(thermalTest,3)
# generate_poles(thermalTest,4)

drawMainWindow()

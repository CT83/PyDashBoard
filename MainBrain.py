from BusinessLogic.Test import Test
from CommonMethods.CommonMethods import display
from CommonVariables.GlobalConstants import application_name, thermalPoles, thermalTestName, thermalFinalResult, \
    thermalContinuous, magneticFinalResult, magneticTestName, magneticPoles, magneticContinuous, TestFinalResult, \
    TestTestName, TestPoles, TestContinuous, Test2FinalResult, Test2TestName, Test2Poles, Test2Continuous
from GUI.PyGenerators import drawMainWindow, generate_new_test, generate_poles

display(application_name + " Initialised...")
display("Generating UI...")

thermalTest = Test(thermalTestName, thermalPoles, thermalContinuous,
                   thermalFinalResult)
generate_new_test(thermalTest)

magneticTest = Test(magneticTestName, magneticPoles, magneticContinuous,
                    magneticFinalResult)
generate_new_test(magneticTest)

testTest = Test(TestTestName, TestPoles, TestContinuous,
                TestFinalResult)
generate_new_test(testTest)

test2Test = Test(Test2TestName, Test2Poles, Test2Continuous,
                 Test2FinalResult)
generate_new_test(testTest)
generate_poles(thermalTest)

drawMainWindow()

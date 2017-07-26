application_name = "PyDashboard"
application_developer = "Rohan Sawant"
application_version_type = "Alpha"
application_version_num = "0.0.1"

MAX_SIZE = 10

# Thermal Test
thermalTestName = "Thermal"
thermalPoles = ["Current1", "Trip", "Time"], \
               ["Current2", "Trip", "Time"], \
               ["Current2", "Trip", "Time"], \
               ["Current3", "Trip", "Time"]

thermalFinalResult = "False"
thermalContinuous = True

# Magnetic Test
magneticTestName = "Magnetic"
magneticPoles = ["Current1", "Trip", "Time"], \
                ["Current2", "Trip", "Time"], \
                ["Current2", "Trip", "Time"], \
                ["Current3", "Trip", "Time"]
magneticFinalResult = "False"
magneticContinuous = "False"

# Test Test
TestTestName = "Electrical"
TestPoles = ["Current1", "Trip", "Time"], \
            ["Current2", "Trip", "Time"], \
            ["Current2", "Trip", "Time"], \
            ["Current3", "Trip", "Time"]
TestFinalResult = "False"
TestContinuous = "False"

# Test Test
Test2TestName = "Sample"
Test2Poles = ["Current1", "Trip", "Time"], \
             ["Current2", "Trip", "Time"], \
             ["Current2", "Trip", "Time"], \
             ["Current3", "Trip", "Time"]
Test2FinalResult = "False"
Test2Continuous = "False"

CURRENT = 0
TIME = 1
IRESULT = 2

ITEMS_EXCEPT_POLES = 1
NUMBER_OF_POLES = 4
TCP_MESSAGE = "D"

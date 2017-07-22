application_name = "PyDashboard"
application_developer = "Rohan Sawant"
application_version_type = "Alpha"
application_version_num = "0.0.1"

MAX_POLE_SIZE = 100

# Thermal Test
thermalTestName = "Thermal"
thermalPoles = ["Current1", "Trip", "Time"], \
               ["Current2", "Trip", "Time"], \
               ["Current3", "Trip", "Time"]
thermalFinalResult = "False"
thermalContinuous = True

# Magnetic Test
magneticTestName = "Magnetic"
magneticPoles = ["Current", "Trip", "Time"], \
                ["Current", "Trip", "Time"], \
                ["Current", "Trip", "Time"]
magneticFinalResult = "False"
magneticContinuous = "False"

# Test Test
TestTestName = "Test"
TestPoles = "Current", "Trip", "Time"
TestFinalResult = "False"
TestContinuous = "False"

# Test Test
Test2TestName = "Test2"
Test2Poles = ["Current", "Trip", "Time"], \
             ["Current", "Trip", "Time"], \
             ["Current", "Trip", "Time"]
Test2FinalResult = "False"
Test2Continuous = "False"

CURRENT = 0
TIME = 1
IRESULT = 2

from CommonMethods.CommonMethods import display
from CommonVariables.GlobalConstants import application_name
from GUI.PyGenerators import drawMainWindow, generateNewTest

display(application_name + " Initialised...")
display("Generating UI...")
drawMainWindow()
generateNewTest()

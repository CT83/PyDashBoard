from threading import Thread

from Communication.Communicator import Communicator
from Communication.Parser import writeCSVtoVariables
from Settings import Settings
from Settings.Settings import *


def initiateBackgroundTasks(self):
    import_settings("Settings.ct83")
    print("Server IP  :" + Settings.SERVER_IP)
    print("Server Port:" + Settings.SERVER_PORT)
    writeCSVtoVariables('''policyID,statecode,county,eq_site_limit,hu_site_limit,fl_site_limit,fr_site_limit,tiv_2011,tiv_2012,eq_site_deductible,hu_site_deductible,fl_site_deductible,fr_site_deductible,point_latitude,point_longitude,line,construction,point_granularity
                        119736,FL,CLAY COUNTY,498960,498960,498960,498960,498960,792148.9,0,9979.2,0,0,30.102261,-81.711777,Residential,Masonry''')

    self.top_PoleTest_T2[0][0].setText("Set by thread")
    self.top_PoleTest_T2[0][2].setText("Set by thread")

    commServer = Communicator(Settings.SERVER_IP, Settings.SERVER_PORT)
    s = Thread(target=Communicator.startServer, args=(commServer,))
    s.daemon = True
    s.start()

    commClient = Communicator(Settings.SERVER_IP, Settings.CLIENT_PORT)
    response = commClient.sendDataRequest()
    writeCSVtoVariables(response)

import csv
from StringIO import StringIO


# The Expected format of the data expected is as folows:
# [SERVER_NAME,STATUS,
# TEST_NO[POLE_NO]]
#######################

def parse_and_write_to_vars(csv_msg):
    buffer = StringIO(csv_msg)
    data = list(csv.reader(buffer))

    print("Done writing CSV to Variables.")

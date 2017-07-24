import csv
from StringIO import StringIO


def writeCSVtoVariables(csv_msg):
    buffer = StringIO(csv_msg)
    data = list(csv.reader(buffer))

    # Write CSV to variables here.

    print("Done writing CSV to Variables.")

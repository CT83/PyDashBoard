import ast


def parse_and_write_to_vars(self, resp):
    print("UnParsed String:" + str(resp))
    resp = ast.literal_eval(resp)
    print("Parsed String:" + str(resp))
    r_index = 0
    for test in xrange(0, 4):
        for pole in xrange(0, 4):
            print("Writing to:" + str(test) + ", " + str(pole))
            r_index = r_index + 1
            self.top_PoleTest_T0[test][pole].setText(resp[r_index])
            r_index = r_index + 1
            self.top_PoleTest_T1[test][pole].setText(resp[r_index])
            r_index = r_index + 1
            self.top_PoleTest_T2[test][pole].setText(resp[r_index])


    print("Done writing CSV to Variables.")

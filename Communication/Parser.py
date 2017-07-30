import ast

red_background = "QLabel { background-color : red; color : white;}"
green_background = "QLabel { background-color : yellow; color : white;}"
orange_background = "QLabel { background-color : pink; color : white;}"
RESP = ["323", "13213"]


def parse_and_write_to_vars(self, resp):
    print("UnParsed String:" + str(resp))
    resp = ast.literal_eval(resp)
    print("Parsed String:" + str(resp))
    r_index = 0
    global RESP
    RESP = resp
    for test in xrange(0, 4):
        for pole in xrange(0, 4):
            print("Writing to:" + str(test) + ", " + str(pole))
            r_index = r_index + 1
            from Tasks import Tasks
            Tasks.invoke_in_main_thread(self.top_PoleTest_T0[test][pole].setText, resp[r_index])
            # self.top_PoleTest_T0[test][pole].setText(resp[r_index])

            # self.top_PoleTest_T0[test][pole].setStyleSheet(choice_back(resp[r_index]))

            r_index = r_index + 1
            #invoke_in_main_thread(self.top_PoleTest_T1[test][pole].setText, resp[r_index])
            # self.top_PoleTest_T1[test][pole].setText(resp[r_index])
            # self.top_PoleTest_T1[test][pole].setStyleSheet(choice_back(resp[r_index]))

            r_index = r_index + 1
            #invoke_in_main_thread(self.top_PoleTest_T2[test][pole].setText, resp[r_index])
            # self.top_PoleTest_T2[test][pole].setText(resp[r_index])
            # self.top_PoleTest_T2[test][pole].setStyleSheet(choice_back(resp[r_index]))

    print("Done writing CSV to Variables.")


def choice_back(i):
    i = int(i)
    if (i % 2 == 0):
        ch = red_background
    else:
        ch = green_background
    return ch

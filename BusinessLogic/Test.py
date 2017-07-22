# add a key to list in dictionary relation ship here.
# pole_list_list is a list of lists which will contain the following
# pole_list[pole number]=[current,time,individual_result]



class Test:
    def __init__(self, test_name, pole_list_list, continuous, final_result):
        self.test_name = test_name
        self.pole_list_list = pole_list_list
        self.result = final_result
        self.continuous = continuous
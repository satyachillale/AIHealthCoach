from pprint import pprint


class Workflow():
    def __init__(self, user_data):
        self.user_data = user_data

    def start_workflow(self):
        print('User data: \n')
        print(self.user_data)

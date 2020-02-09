class Command:
    def __init__(self, command_type, *args):
        self.commandType = command_type
        self.args = args

    def set_args(self, *args):
        self.args = args

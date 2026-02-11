class CommandRouter:
    def __init__(self):
        self.routes = {}

    def register(self, command_name, handler):
        self.routes[command_name.upper()] = handler

    def dispatch(self, command):
        command = command.upper()
        if command in self.routes:
            self.routes[command]()
        else:
            print("Invalid command.")
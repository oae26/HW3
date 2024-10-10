from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

class App:
    def __init__(self): #Constructor
        self.command_handler = CommandHandler()
        # Register commands here

    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())

        print("Type 'exit' to exit.")
        while True: #Repl Read, Evaluate,  Process, Loop
            self.command_handler.execute_command(input(">>>").strip())
def start(self):
    self.command_handler.register_command("greet", GreetCommand())
    self.command_handler.register_command("goodbye", GoodbyeCommand())
    self.command_handler.register_command("exit", ExitCommand())
    
    print("Type 'exit' to exit the app")
    while True: #REPL, Read, Evaluate, Process, Loop
        self.command_handler.execute_command(input(">>>").strip())
    
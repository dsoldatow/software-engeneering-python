from commands.commands import Commands

if __name__ == "__main__":
    while True:
        command = input('input your command < ')
        command = command.split()
        obj = None
        if len(command) >1:
            obj = command[1].lower()
        if Commands.get(command[0]) is not None:
            Commands[command[0].lower()].run(object=obj)
        else:
            print('command not found')

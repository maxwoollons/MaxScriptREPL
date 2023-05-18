print("Welcome to the adder REPL")
print("Enter 'quit' to quit")

loop = True
variables = {}
while loop:
    command = input("??? ")
    if command == "quit":
        loop = False
    elif command.startswith("input"):
        variable_name = command[6:]
        variable_value = input("Enter a value for " + variable_name + ": ")
        variables[variable_name] = variable_value
    elif command.startswith("print"):
        variable_name = command[6:]
        if variable_name in variables:
            print(variables[variable_name])
        else:
            print(variable_name)
    elif " gets " in command:
        variable_name = command[:command.find(" gets ")]
        variable_value = command[command.find(" gets ") + 6:]
        if variable_value in variables:
            variables[variable_name] = variables[variable_value]
        else:
            variables[variable_name] = variable_value
    elif " adds " in command:
        variable_name = command[:command.find(" adds ")]
        variable_value = command[command.find(" adds ") + 6:]
        if variable_value in variables:
            variables[variable_name] = int(variables.get(variable_name, 0)) + int(variables[variable_value])
        else:
            variables[variable_name] = int(variables.get(variable_name, 0)) + int(variable_value)    
            variables[variable_name] = int(variables[variable_name]) + int(variable_value)
    else:
        print("Syntax error.")






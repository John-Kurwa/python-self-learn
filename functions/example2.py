# Python Function Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
def greetUser(greeting, name):
    return f"{name}, {greeting}!"

message = greetUser("Good Morning", "Alice")
print(message)

# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that is passed into a function.
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.

# Default Parameter Values
def taskStatus(task = "Incomplete"):
    print("Status:", task)
taskStatus()
taskStatus("Complete")

def greetUserWithDefault(name, greeting="Hello"):
    return f"{name}, {greeting}!"
messageWithDefault = greetUserWithDefault("Bob")
print(messageWithDefault)





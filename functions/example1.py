# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# Why Use Functions? - Avoiding repetition, improving readability, and modularity.

def myFunction():
    print("Hello World")

myFunction()

# Return Values
def scheduleMeeting(day, time):
    return f"Meeting scheduled on {day} at {time}"

meetingDetails = scheduleMeeting("Monday", "10:00 AM")
print(meetingDetails)

# The pass Statement
def placeholderFunction():
    pass
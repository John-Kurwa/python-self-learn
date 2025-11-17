# if statement
# Evaluates a condition (an expression that results in True or False).
# If the condition is true, the code block inside the if statement is executed. 
# If the condition is false, the code block is skipped

age = 18
if age >= 18: print("You are an adult.") 
    
# Elif Keyword
# Way of saying "if the previous conditions were not true, then try this condition".
# You can have as many elif statements as you need.
# Python will check each condition in order and execute the first one that is true.
age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18:
    print("You are an adult.")

# Else Keyword
# Catches anything which isn't caught by the preceding conditions.
age = 28
if age <= 13:
    print("You are an Alpha.")
elif age >= 14 and age <= 28:
    print("You are Gen Z.")
elif age > 28 and age <= 46:
    print("You are a Millennial.")
else:
    print("You are Gen X or older.")

# Nested If
# An if statement inside another if statement.
num = 8
if num > 0:
    print("The number is positive,")
    if num % 2 == 0:
        print("and even.")
    else:
        print("The number is positive and odd.")

# Pass Statement
# Used when a statement is required syntactically but you do not want any command or code to execute.
# Used as a placeholder.
num = 10
if num > 0:
    pass 
   

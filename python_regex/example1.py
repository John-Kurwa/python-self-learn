# Metacharacters in Regular Expressions
# [] Matches any single character within the brackets
import re

matchday = "Brighton Hove Albion vs Manchester United 2024-08-25"
x = re.findall("[a-p]", matchday)
print(x)

# \ Signals a special sequence (can also be used to escape special characters)	
x = re.findall("\d", matchday)  #find all digits
print(x)

# . Any character (except newline character)
x = re.findall("Ma.......r", matchday)  
print(x)

# ^  starts with
x = re.findall("^Brighton", matchday)
print(x)

# $  ends with
x = re.findall("2024-08-25$", matchday)
if x:
    print("Yes, the string ends with '2024-08-25'")
else:
    print("No match")

# *  zero or more occurrences
x = re.findall("a.*n", matchday)
print(x)

# + one or more occurrences
x = re.findall("a.+n", matchday)
print(x)

# {} Exactly the specified number of occurrences
x = re.findall("Ma.{7}r", matchday)
print(x)

# ?  Zero or one occurrence
x = re.findall("M.?n", matchday)
print(x)

# | Either or
x = re.findall("Brighton|Manchester", matchday)
print(x)

# () Capture and group
x = re.findall("(Brighton|Manchester) United", matchday)
print(x)
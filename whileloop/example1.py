# while loop we can execute a set of statements as long as a condition is true.
# remember to increment i, or else the loop will continue forever.
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# break_statement - can stop the loop even if the while condition is true
# i = 1
# while i < 4:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# continue_statement - stops the current iteration, and continues with the next
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# else_statement - runs a block of code once when the condition is false
i = 1
while i < 4:
  print(i)
  i += 1    
else:
  print("i is no longer less than 4")
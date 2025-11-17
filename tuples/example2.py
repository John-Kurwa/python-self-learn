# Unpacking a Tuple
fruits = ("cherry", "strawberry", "raspberry")
(green, yellow, red) = fruits

print(green)
print(yellow)   
print(red)

# Using Asterisk*
fruits = ("cherry", "strawberry", "raspberry")
(*red,) = fruits
print(red)

# Loop through a Tuple
for x in fruits:
    print(x)
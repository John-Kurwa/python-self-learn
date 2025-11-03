# python - Modify strings
# upper case
name  = "Heisenberg"
print(name.upper())  # HEISENBERG
# lower case
print(name.lower())  # heisenberg

# remove whitespace
txt = "   Hello, World!   "
print(txt.strip())  # "Hello, World!"

# replace string
print(name.replace("H", "J"))  # Jeisenberg

# split string
txt2 = "apple, banana, cherry"
print(txt2.split(", "))  # ['apple', 'banana', 'cherry']

# check string
txt3 = "Hello, World!"
print("World" in txt3)  # True

# concatenate strings
first_name = "Walter"
last_name = "White"
full_name = first_name + " " + last_name
print(full_name)  # Walter White

# format strings
age = 50
txt4 = "My name is {} and I am {} years old."
print(txt4.format(full_name, age))  # My name is Walter White and I am 50 years old.

# escape characters
print("He said, \"I am the one who knocks!\"")  # He said, "I am the one who knocks!"

# find string
print(name.find("sen"))  # 2

# count occurrences
print(txt3.count("l"))  # 3

# check start and end
print(txt3.startswith("Hello"))  # True

print(txt3.endswith("!"))  # True
# join strings
my_list = ["Hello", "World"]
print(" ".join(my_list))  # Hello World
# string formatting with f-strings
print(f"{first_name} {last_name} is {age} years old.")  # Walter White is 50 years old.
# string encoding
encoded_txt = txt3.encode("utf-8")
print(encoded_txt)  # b'Hello, World!'
# string decoding
decoded_txt = encoded_txt.decode("utf-8")
print(decoded_txt)  # Hello, World!
# string alignment
print(txt3.ljust(20, '-'))  # Hello, World!-------
print(txt3.rjust(20, '-'))  # -------Hello, World!
print(txt3.center(20, '-'))  # ----Hello, World!----
# string partition
print(txt3.partition(", "))  # ('Hello', ', ', 'World!')
# string zfill
print(name.zfill(15))  # 00000Heisenberg
# string title case
print(name.title())  # Heisenberg
# string swap case
print(name.swapcase())  # hEISENBERG
# string casefold
print(name.casefold())  # heisenberg
# string isalpha
print(name.isalpha())  # True
# string isdigit
print("12345".isdigit())  # True
# string isspace
print("   ".isspace())  # True
# string istitle
print("Hello World".istitle())  # True
# string islower
print("hello".islower())  # True
# string isupper
print("HELLO".isupper())  # True
# string maketrans and translate

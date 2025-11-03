# Many Values to Multiple Variables
h, i, j = 'BMW', 'Audi', 'GTR'
print(h)
print(i)    
print(j)

print('---')
# One Value to Multiple Variables
x = y = z = 'Audi'
print(x)
print(y)    
print(z)

print('---')
# Unpacking a Collection
fruits = ['apple', 'banana', 'cherry']
m, n, o = fruits
print(m)
print(n)    
print(o)

print('---')
# output variables
view = 'This is Kenya'
print(view)

print('---')
# Global Variable
x = "awesome"

def myfunc():
    print("Learning Python is " + x)

myfunc()
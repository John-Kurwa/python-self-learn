# Generators
def printer():
    yield "Hello"
    yield "from"
    yield "Yohana"

for x in printer():
    print(x)

def count_num(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for x in count_num(7):
    print(x)

# Using next() with Generators 
def songs():
    yield "Backbencher"
    yield "Donjo Maber"
    yield "Nahumanyane"

song_generator = songs()
print(next(song_generator))
print(next(song_generator))
print(next(song_generator))

# Generator Expressions
squares = [x * x for x in range(1, 6)]
print(squares)

sqr_exp = (x * x for x in range(1, 6))
for num in sqr_exp:

    print(num)
    print(list(sqr_exp))

# close ()
def colors():
    try:        
        yield "Red"
        yield "Green"
        yield "Blue"
    finally:
        print("N0 more colors.")

color_gen = colors()
print(next(color_gen))
color_gen.close()
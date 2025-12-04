# Looping Through an Iterator
my_iter = iter(["Maputo", "Accra", "Kigali", "", "Nairobi"])

for value in my_iter:
    print(value)

# Create an iterator from a string
str_iter = iter("Africa")
for char in str_iter:
    print(char)

print("-----")
# Create an Iterator
class CountDown:
    def __init__(self, start):
        self.x = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= 0:
            raise StopIteration
        else:
            self.x -= 1
            return self.x + 1
countdown = CountDown(7)
for number in countdown:
    print(number)
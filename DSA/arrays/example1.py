# Minimum value in an array
def find_minimum(arr):
    if not arr:
        return None  # Return None if the array is empty
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value    
# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
minimum_value = find_minimum(array) 
print(f"The minimum value in the array is: {minimum_value}")

arr = [10, 20, 5, 40, 15]
minVal = arr[0]

for y in arr:
    if y < minVal:
        minVal = y

print("The lowest number is:",minVal)
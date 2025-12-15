# The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
# Example usage
array = [33, 10, 55, 26, 19, 42, 8]
sorted_arr = quicksort(array)   
print("Sorted array:", sorted_arr)

# Example 2
# Defines a function to partition the array around a pivot
def partition(array, low, high):
# Chooses the last element as pivot
    pivot = array[high]
# Tracks the boundary of smaller than or equal to the pivot element
    i = low - 1
# Loops through each element in the array
    for j in range(low, high):
        if array[j] <= pivot:
# Move the boundary (i) forward
# Swap the smaller element into the left (smaller) section
# This ensures:
# Elements ≤ pivot go to the left
# Elements > pivot stay on the right
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1
# This function recursively sorts the array.
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
# Ensures there are at least two elements to sort
# Prevents unnecessary recursion
    if low < high:
        pivot_index = partition(array, low, high)
# Recursively sorts the left side of the pivot
        quicksort(array, low, pivot_index-1)
# Recursively sorts the right side of the pivot
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
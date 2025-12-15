# Insertion Sort
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.
def insert_sort(arr):
    n = len(arr)
    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Example usage
array = [12, 11, 13, 5, 6]
sorted_arr = insert_sort(array)
print("Sorted array:", sorted_arr)
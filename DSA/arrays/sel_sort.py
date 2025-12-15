# Selection Sort
# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
def sel_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Example usage
array = [64, 25, 12, 22, 11]
sorted_arr = sel_sort(array)
print("Sorted array:", sorted_arr)
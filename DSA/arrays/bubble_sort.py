# Bubble Sort 
# The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.
def b_sort (arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already sorted
        for j in range(n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr
# Example usage
array = [68, 34, 25, 12, 22, 55, 92, 6, 3]
sorted_arr = b_sort(array)
print("Sorted array:", sorted_arr)
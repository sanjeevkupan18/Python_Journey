def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", unsorted_list)

bubble_sort(unsorted_list)
print("Sorted list:", unsorted_list)
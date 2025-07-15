# Python program for Linear Search using iterative approach
def linear_search(arr, target):
    # Traverse through all elements in the array
    for index in range(0,n):
        # If the element is found, return its index
        if arr[index] == target:
            return index
    # If the element is not found, return -1
    return -1

# Example usage:
n=int(input("Enter the list size :"))
arr = []
for i in range(0,n):
    l=int(input("Enter Values :"))
    arr.append(l)

target = int(input("Enter the target value :"))

# Function call
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
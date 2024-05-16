def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement
    return arr

arr = list(map(int, input("Enter the array of integers separated by spaces: ").split()))

sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

target = int(input("Enter the target element to search for: "))

if target in sorted_arr:
    replacement = int(input("Enter the replacement element: "))
    
    modified_arr = replace_elements(sorted_arr, target, replacement)
    print("Modified array after replacing elements:", modified_arr)
else:
    print("Target element not found in the array.")

from typing import List


def merge_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[mid:])    # sort half
    right = merge_sort(arr[:mid])   # sort other half

    i = j = k = 0
    # copy data to arr
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


def print_array(arr: list):
    for a in arr:
        print(a, end=" ")
    print("\n")


array = [1, 3, 2, 7, 2, 0]
print_array(array)
merge_sort(array)
print_array(array)

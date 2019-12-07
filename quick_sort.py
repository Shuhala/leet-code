from typing import List


def quick_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr

    less = []
    equal = []
    greater = []

    pivot = arr[0]
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + equal + quick_sort(greater)


def print_array(arr: list):
    for a in arr:
        print(a, end=" ")
    print("\n")


array = [1, 3, 2, 7, 2, 0]
print_array(array)
array = quick_sort(array)
print_array(array)

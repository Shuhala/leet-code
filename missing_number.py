def search(ar):
    a = 0
    b = len(ar)
    mid = 0
    while b > a + 1:
        mid = (a + b) // 2
        if ar[mid] == mid + 1:
            a = mid
        else:
            b = mid
        # if (ar[a] - a) != (ar[mid] - mid):
        #     b = mid
        # elif (ar[b] - b) != (ar[mid] - mid):
        #     a = mid
    return ar[mid] - 1


# Driver Code

print("Missing number:", search([1, 2, 3, 4, 5, 6, 8]))

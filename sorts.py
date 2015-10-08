

def quicksort(arr):

    # take first element as pivot
    # recurively sort lesser and greater numbers
    
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater


def merge(a, b):

    # helper function to actually merge two lists

    if a[0] > b[0]:
        return merge(b, a)

    i = 0; j = 0; lst = []

    while i < len(a) or j < len(b):

        if i == len(a):
            lst.append(b[j])
            j += 1

        elif j == len(b):
            lst.append(a[i])
            i += 1

        elif a[i] <= b[j]:
            lst.append(a[i])
            i += 1
        
        elif a[i] > b[j]:
            lst.append(b[j])
            j += 1

    return lst


def mergesort(arr):

    # split array into smaller and smaller pieces
    # then merge from bottom up

    if len(arr) <= 1:
        return arr

    mid = len(arr) / 2
    a = mergesort(arr[:mid])
    b = mergesort(arr[mid:])

    return merge(a, b)


print quicksort([3,77,45,2,7])
print mergesort([3,77,45,2,7])


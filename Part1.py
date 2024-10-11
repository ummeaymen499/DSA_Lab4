def PARTITION(A, p, r):
    pivot = A[r - 1]
    i = p
    for j in range(p, r - 1):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r - 1] = A[r - 1], A[i]
    return i

def QUICKSORT(A, p, r):
    if r - p <= 1:
        return
    else:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q)
        QUICKSORT(A, q + 1, r)

if __name__ == "__main__":
    arr = [8, 7, 1, 3, 5, 6, 4]
    QUICKSORT(arr, 0, len(arr))
    print(arr)

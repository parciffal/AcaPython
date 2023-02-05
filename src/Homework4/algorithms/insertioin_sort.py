def insertion_sort(A: list):
    for i in range(2, len(A)):
        key = A[i]
        j = i-1
        while j > 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


m = [1, 3, 23, 5, 1, 2]

print(insertion_sort(m))
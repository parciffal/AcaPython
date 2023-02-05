def counting_sort(arr):
    k = max(arr) + 1
    count = [0]*k
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(k):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr
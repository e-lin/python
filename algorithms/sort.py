def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(data):
    if len(data) <= 1:
        return data
    middle = int(len(data)/2)
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])
    result = merge(left, right)
    return result

def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = quicksort([d for d in data[1:] if d < pivot])
    large = quicksort([d for d in data[1:] if d >= pivot])
    return less + [pivot] + large

def insertion_sort(data):
    for i in range(len(data)):
        j = i
        while j > 0 and data[j-1] > data[j]:
            data[j-1], data[j] = data[j], data[j-1]
            j -= 1
    return data

import heapq
def heapsort(data):
    # heapq.heapify creates heap from a list in linear time
    heapq.heapify(data)
    return [heapq.heappop(data) for i in range(len(data))]


l = [9,2,3,4,7]
# print mergesort(l)
# print quicksort(l)
# print insertion_sort(l)
print heapsort(l)


def max_heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)

    # Start from the last non-leaf node and heapify all nodes in reverse order
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

# Input array
arr = [9, 4, 7, 2, 5, 1, 8, 6, 3]

# Build a max heap from the input array
build_max_heap(arr)

# Print the transformed max heap
print("Transformed Max Heap:", arr)

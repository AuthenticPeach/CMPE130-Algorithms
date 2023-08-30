import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element

# Generate a large list of random numbers
large_list = [random.randint(1, 1000) for _ in range(10000)]

print("Original List: [First few elements]", large_list[:10], "...")

start_time = time.time()  # Record the start time
insertion_sort(large_list)
end_time = time.time()    # Record the end time

print("Sorted List: [First few elements]", large_list[:10], "...")

running_time = end_time - start_time
print("Running Time: {:.6f} seconds".format(running_time))

print("Best Case Time Complexity: O(n)")
print("Worst Case Time Complexity: O(n^2)")

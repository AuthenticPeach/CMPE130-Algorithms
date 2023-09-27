def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"Array: {arr}")
    print(f"Pivot: {pivot}")
    print(f"Left: {left}")
    print(f"Middle: {middle}")
    print(f"Right: {right}")

    return quicksort(left) + middle + quicksort(right)

# Example usage:
if __name__ == "__main__":
    input_array = [3, 6, 8, 10, 1, 2, 1]
    print("Input Array:", input_array)
    sorted_array = quicksort(input_array)
    print("Sorted Array:", sorted_array)

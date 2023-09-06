def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Print the current subarray being sorted
    print("Splitting:", arr)

    # Split the input list into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively apply merge_sort to both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    result = []
    left_index = right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

    # Append the remaining elements, if any
    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])

    # Print the merged result
    print("Merging:", result)

    return result

# Demonstrate Merge Sort
if __name__ == "__main__":
    input_list = [12, 11, 13, 5, 6, 7]
    print("Input List:", input_list)

    sorted_list = merge_sort(input_list)
    print("Sorted List:", sorted_list)

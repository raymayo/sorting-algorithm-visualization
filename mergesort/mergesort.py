# Given array to be sorted
array = [38, 27, 43, 3, 9, 82, 10]


# Merge sort function
def merge_sort(array):
    # Base case: If the array has 1 or 0 elements, it is already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursive calls to sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


# Merge function to merge two sorted halves
def merge(left, right):
    # Initialize an empty list to store the merged result
    result = []

    # Initialize indices for the left and right halves (both set to 0 initially)
    left_index = right_index = 0

    # Compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        # Compare elements from both halves and merge them in sorted order
        if left[left_index] < right[right_index]:
            # If the element in the left half is smaller, append it to the result
            result.append(left[left_index])
            # Move the index to the next element in the left half
            left_index += 1
        else:
            # If the element in the right half is smaller or equal, append it to the result
            result.append(right[right_index])
            # Move the index to the next element in the right half
            right_index += 1

    # Add the remaining elements from both halves (if any)
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


# Example usage:

# Sort the given array using merge sort
sorted_arr = merge_sort(array)

# Print the original and sorted arrays
print("Original Array:", array)
print("Sorted Array:", sorted_arr)

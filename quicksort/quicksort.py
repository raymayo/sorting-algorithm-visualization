# Array example
ARRAY = [3, 6, 8, 10, 1, 2, 1]


# Quicksort function
def quicksort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as the pivot
        pivot = arr[0]

        # Partition the array into two subarrays:
        # 1. Elements less than or equal to the pivot
        # 2. Elements greater than the pivot
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        # Recursively apply quicksort on the subarrays
        return quicksort(less) + [pivot] + quicksort(greater)


# Example usage:
SORTED_LIST = quicksort(ARRAY)
print(SORTED_LIST)

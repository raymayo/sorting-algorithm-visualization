def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        smaller_elements = [x for x in array[1:] if x <= pivot]
        larger_elements = [x for x in array[1:] if x > pivot]
        return quicksort(smaller_elements) + [pivot] + quicksort(larger_elements)

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = quicksort(my_list)
print(sorted_list)
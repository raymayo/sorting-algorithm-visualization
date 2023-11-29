import matplotlib.pyplot as plt
import numpy as np
import random

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)
        plot_and_pause(arr, start, mid, end)

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def plot_and_pause(arr, start, mid, end):
    plt.clf()

    # Set the figure to fullscreen mode
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')  # Maximize the window on Windows

    colors = ['lightblue'] * len(arr)
    
    # Highlight all elements inside the merging subarrays in orange
    for i in range(start, end + 1):
        colors[i] = '#F3B51E'
    
    # Add an outline to all bars
    edgecolors = ['black' for _ in colors]
    
    # Set all bars to 'lightgreen' after sorting is complete
    if start == 0 and end == len(arr) - 1:
        plt.title(f'Merge Sort')
        colors = ['lightgreen'] * len(arr)
    else:
        plt.title(f'Merge Sort')
    
    plt.bar(range(len(arr)), arr, color=colors, edgecolor=edgecolors)
    plt.pause(0.1)

# Example usage
arr = random.sample(range(1, 101), 100)
plt.ion()  # Turn on interactive mode for live plotting
merge_sort(arr, 0, len(arr) - 1)
plt.ioff()
plt.show()

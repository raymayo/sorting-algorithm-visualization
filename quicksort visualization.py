import matplotlib.pyplot as plt
import numpy as np

def quicksort(array, low, high, ax):
    if low < high:
        pivot_index = partition(array, low, high, ax)
        quicksort(array, low, pivot_index - 1, ax)
        quicksort(array, pivot_index + 1, high, ax)

def partition(array, low, high, ax):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            visualize_sorting(array, high, i, j, ax)

    array[i + 1], array[high] = array[high], array[i + 1]
    visualize_sorting(array, i + 1, i + 1, high, ax)

    return i + 1

def visualize_sorting(array, pivot_index, low, high, ax, sorting_complete=False):
    ax.clear()
    if sorting_complete:
        ax.bar(range(len(array)), array, color='lightgreen', edgecolor='black')
    else:
        ax.bar(range(len(array)), array, color='lightblue', edgecolor='black')
        ax.bar(pivot_index, array[pivot_index], color='#F3B51E', edgecolor='black', label='Pivot')
        ax.bar(low, array[low], color='lightgreen', edgecolor='black', label='Less Than Pivot')
        ax.bar(high, array[high], color='#FE5D25', edgecolor='black', label='Greater Than Pivot')
        ax.legend()
    plt.pause(0.15)

def main_sorting_visualization():
    array = np.random.randint(1, 100, size=50)
    print("Original array:", array)

    fig, ax = plt.subplots()
    fig.set_facecolor('#E0E0E0')
    ax.set_facecolor('#f0f0f0')
    ax.bar(range(len(array)), array, color='lightblue', edgecolor='black')
    plt.pause(.1)

    # Maximize the window if using Tkinter backend
    manager = plt.get_current_fig_manager()
    try:
        manager.window.state('zoomed')  # for Windows
    except AttributeError:
        try:
            manager.window.attributes('-zoomed', True)  # for Linux
        except AttributeError:
            pass  # for MacOS

    quicksort(array, 0, len(array) - 1, ax)
    visualize_sorting(array, pivot_index=0, low=0, high=0, ax=ax, sorting_complete=True)

    plt.show(block=True)
    print("Sorted array:", array)

if __name__ == "__main__":
    main_sorting_visualization()

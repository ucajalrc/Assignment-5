import random

def randomized_quicksort(arr):
    """
    Sorts an array in place using the Randomized Quicksort algorithm.
    This version chooses the pivot randomly in each recursive step, 
    greatly reducing the chance of worst-case (O(n^2)) performance.
    On average, this runs in O(n log n) time for all input orders.
    """

    def quicksort_helper(array, low, high):
        """
        Recursively sorts the array from index 'low' to 'high' (inclusive).
        """
        if low < high:
            # Select a random pivot and swap it with the last element
            pivot_index = random.randint(low, high)
            array[pivot_index], array[high] = array[high], array[pivot_index]
            # Partition the array using the random pivot
            p = partition(array, low, high)
            # Recursively sort left and right parts
            quicksort_helper(array, low, p - 1)
            quicksort_helper(array, p + 1, high)

    def partition(array, low, high):
        """
        Standard Lomuto partitioning.
        The pivot is now at array[high].
        All elements <= pivot go to the left.
        """
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    # Main entry point: sort the full array if not empty or one element
    if arr is None or len(arr) <= 1:
        return arr
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr

# Example usage:
# if __name__ == "__main__":
#     sample = [10, 4, 6, 2, 8, 1]
#     print("Original:", sample)
#     randomized_quicksort(sample)
#     print("Sorted:", sample)

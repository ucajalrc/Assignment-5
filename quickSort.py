def quicksort(arr):
    """
    Sorts an array in place using the classic deterministic Quicksort algorithm.
    This version always chooses the last element of the subarray as the pivot.
    It is efficient for most random data, but can be slow (O(n^2)) if the data is already sorted or reverse sorted.
    """

    def quicksort_helper(array, low, high):
        """
        Recursively sorts the array from index 'low' to 'high' (inclusive).
        """
        if low < high:
            # Partition the array and get the final position of the pivot
            pivot_index = partition(array, low, high)
            # Recursively sort elements before and after the pivot
            quicksort_helper(array, low, pivot_index - 1)
            quicksort_helper(array, pivot_index + 1, high)

    def partition(array, low, high):
        """
        Partitions the subarray using the last element as the pivot.
        All elements less than or equal to the pivot are moved to the left.
        Returns the index where the pivot ends up.
        """
        pivot = array[high]          # Choose pivot (last element)
        i = low - 1                  # Index of smaller element
        # Move elements <= pivot to the left
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        # Place the pivot after all smaller elements
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    # Main entry point: sort the full array if not empty or one element
    if arr is None or len(arr) <= 1:
        return arr
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr

# Example usage:
# if __name__ == "__main__":
#     sample = [3, 7, 2, 9, 1, 5]
#     print("Original:", sample)
#     quicksort(sample)
#     print("Sorted:", sample)

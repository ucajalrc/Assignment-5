import random
import time
import copy

from quickSort import quicksort
from randomizedQuicksort import randomized_quicksort

def benchmark(sort_func, data):
    """
    Times how long it takes to sort a copy of 'data' using the provided sorting function.
    Returns the time in seconds, or None if a RecursionError occurs (for large, bad cases).
    """
    arr = copy.deepcopy(data)  # So the original isn't modified!
    try:
        start = time.perf_counter()
        sort_func(arr)
        end = time.perf_counter()
        return end - start
    except RecursionError:
        return None

if __name__ == "__main__":
    sizes = [500,1000, 5000]  # Feel free to add larger sizes for randomized_quicksort!
    distributions = {
        "Random": lambda n: [random.randint(0, n) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
    }

    print(f"{'Array Size':>10} | {'Type':>10} | {'Deterministic (s)':>18} | {'Randomized (s)':>15}")
    print("-" * 62)

    for n in sizes:
        for dist_name, generator in distributions.items():
            data = generator(n)
            t_det = benchmark(quicksort, data)
            t_rand = benchmark(randomized_quicksort, data)
            t_det_str = f"{t_det:.5f}" if t_det is not None else "RecursionError"
            t_rand_str = f"{t_rand:.5f}" if t_rand is not None else "RecursionError"
            print(f"{n:>10} | {dist_name:>10} | {t_det_str:>18} | {t_rand_str:>15}")

    print("\nNote: If you see 'RecursionError', that means the deterministic quicksort exceeded Python's recursion limit (expected for large, sorted inputs).")

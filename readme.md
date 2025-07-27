# Assignment 5: Quicksort Algorithm — Implementation, Analysis, and Randomization

## Overview

This repository contains:
- Implementations of both deterministic and randomized Quicksort in Python
- A benchmarking script for empirical analysis and comparison
- A detailed written report in `report.docx` or `report.pdf`) with code snapshots, and analysis

## Files Included

- **`quicksort.py`**  
  Deterministic Quicksort implementation (last element as pivot).  

- **`randomized_quicksort.py`**  
  Randomized Quicksort implementation (random pivot at each step).  

- **`benchmark.py`**  
  Script to empirically compare both sorting algorithms.  
  Tests on random, sorted, and reverse-sorted arrays and prints results in a table.

- **`report.docx`**
  The assignment report with beginner-friendly explanations, performance analysis, theoretical discussion, sample results, and APA references.

## How to Run

1. **Install Python 3.x** (recommended: Python 3.7 or newer).

2. **Clone or download this repository** and navigate to the folder.

3. **To benchmark both Quicksort versions:**
   ```sh
   python3 benchmark.py

4. **To run deterministic quick sort (uncomment the main section first):**
   ```sh
   python3 quickSort.py

5. **To run randomized quick sort (uncomment the main section first):**
   ```sh
   python3 randomizedQuicksort.py
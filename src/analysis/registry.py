from src.sorting_algorithms import (
    insertion_sort,
    shell_sort1,
    shell_sort2,
    shell_sort3,
    shell_sort4,
    shell_sort5,
    tim_sort,
)
from .distributions import (
    fisher_yates,
    almost_sorted,
    two_alternating_runs,
)

ALGORITHMS = {
    "insertion sort" : insertion_sort,
    "shell sort 1" : shell_sort1,
    "shell sort 2" : shell_sort2,
    "shell sort 3" : shell_sort3,
    "shell sort 4" : shell_sort4,
    "shell sort 5" : shell_sort5,
    "tim sort" : tim_sort,
}

DISTRIBUTIONS = {
    "Uniformly Distributed Permutations" : fisher_yates,
    "Almost-Sorted Permutations" : almost_sorted,
    "Two Alternating Runs Permutation" : two_alternating_runs,
}
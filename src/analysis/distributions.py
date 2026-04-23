import random
import math

def fisher_yates(nums : list[int], seed : int | None = None) -> list[int]:
    rng = random.Random(seed)
    uniformly_random_perm = nums[:]
    n = len(uniformly_random_perm)

    if n <= 1:
        return uniformly_random_perm

    for k in range(n-1, 0, -1):
        j = rng.randint(0, k)
        uniformly_random_perm[k], uniformly_random_perm[j] = (uniformly_random_perm[j], uniformly_random_perm[k],)
    
    return uniformly_random_perm


def almost_sorted(nums : list[int], seed : int | None = None) -> list[int]:
    rng = random.Random(seed)
    almost_sorted_perm = sorted(nums)
    n = len(almost_sorted_perm)

    if n <= 1:
        return almost_sorted_perm

    num_swaps = int(math.log2(n))
    for _ in range(num_swaps):
        i = rng.randint(0, n - 1)
        j = rng.randint(0, n - 1)
        almost_sorted_perm[i], almost_sorted_perm[j] = (almost_sorted_perm[j], almost_sorted_perm[i])
    
    return almost_sorted_perm


def two_alternating_runs(nums : list[int], seed : int | None = None) -> list[int]:
    base = sorted(nums)

    odds = base[::2]
    evens = base[1::2]

    return odds + evens

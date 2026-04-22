import random
import math

class ListDistributionGenerator:
    '''
    Generates controlled distributions of an input list for empirical
    analysis of sorting algorithms.

    This class takes an initial list and produces multiple variants that
    simulate different input conditions. A fixed seed is used to ensure reproducibility of
    experiments.

    The original data remains unchanged; all methods return new lists.
    '''
    def __init__(self, nums : list[int], seed : int):
        self.nums = nums
        self.rng = random.Random(seed)
    

    def fisher_yates(self) -> list[int]:
        uniformly_random_perm = self.nums[:]
        n = len(uniformly_random_perm)

        if n <= 1:
            return uniformly_random_perm

        for k in range(n-1, 0, -1):
            j = self.rng.randint(0, k)
            uniformly_random_perm[k], uniformly_random_perm[j] = (uniformly_random_perm[j], uniformly_random_perm[k],)
        
        return uniformly_random_perm

    def almost_sorted(self) -> list[int]:
        almost_sorted_perm = self.nums[:]
        almost_sorted_perm.sort()
        n = len(almost_sorted_perm)

        if n <= 1:
            return almost_sorted_perm

        num_swaps = int(math.log2(n))
        for k in range(num_swaps):
            i = self.rng.randint(0, n - 1)
            j = self.rng.randint(0, n - 1)
            almost_sorted_perm[i], almost_sorted_perm[j] = (almost_sorted_perm[j], almost_sorted_perm[i])
        
        return almost_sorted_perm
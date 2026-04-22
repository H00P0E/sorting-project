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

        for k in range(n-1, 0, -1):
            j = self.rng.randint(0, k)
            uniformly_random_perm[k], uniformly_random_perm[j] = (uniformly_random_perm[j], uniformly_random_perm[k],)
        
        return uniformly_random_perm
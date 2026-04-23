from .registry import (ALGORITHMS, DISTRIBUTIONS)

class Experiment:
    def __init__(self, sorting_algorithm : str, distribution : str, input_size : int, seed : int):
        self.sorting_algorithm = sorting_algorithm
        self.distribution = distribution
        self.input_size = input_size
        self.seed = seed
    
    def experiment_runner(self) -> int:
        if self.sorting_algorithm not in ALGORITHMS:
            raise ValueError(f"Unknown algorithm: {self.sorting_algorithm}")
        if self.distribution not in DISTRIBUTIONS:
            raise ValueError(f"Unknown distribution: {self.distribution}")
        
        input_list = list(range(self.input_size))

        generated = DISTRIBUTIONS[self.distribution](input_list, self.seed)
        expected = sorted(generated)
        nums = generated.copy()

        comparisons = ALGORITHMS[self.sorting_algorithm](nums)

        if nums != expected:
            raise ValueError(f"{self.sorting_algorithm} failed on {self.distribution} input of size {self.input_size}")

        return comparisons
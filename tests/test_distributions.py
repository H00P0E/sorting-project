from src.analysis.distributions import ListDistributionGenerator

from collections import Counter

################################
# TEST FISHER-YATES:
################################
def test_fisher_yates_preserves_elements():
    gen = ListDistributionGenerator([5, 2, 4, 1, 3], 42)
    shuffled = gen.fisher_yates()

    assert len(shuffled) == 5
    assert sorted(shuffled) == [1, 2, 3, 4, 5]


def test_fisher_yates_preserves_duplicates():
    nums = [3, 1, 3, 2, 2]
    gen = ListDistributionGenerator(nums, 42)
    shuffled = gen.fisher_yates()

    assert len(shuffled) == len(nums)
    assert sorted(shuffled) == sorted(nums)


def test_fisher_yates_does_not_modify_original():
    nums = [5, 2, 4, 1, 3]
    gen = ListDistributionGenerator(nums, 42)

    shuffled = gen.fisher_yates()

    assert nums == [5, 2, 4, 1, 3]
    assert shuffled is not nums


def test_fisher_yates_same_seed_same_output():
    nums = [5, 2, 4, 1, 3]

    gen1 = ListDistributionGenerator(nums, 42)
    gen2 = ListDistributionGenerator(nums, 42)

    shuffled1 = gen1.fisher_yates()
    shuffled2 = gen2.fisher_yates()

    assert shuffled1 == shuffled2


def test_fisher_yates_empty():
    gen = ListDistributionGenerator([], 42)
    assert gen.fisher_yates() == []


def test_fisher_yates_single_element():
    gen = ListDistributionGenerator([7], 42)
    assert gen.fisher_yates() == [7]


def test_fisher_yates_two_elements():
    gen = ListDistributionGenerator([1, 2], 42)
    shuffled = gen.fisher_yates()
    assert sorted(shuffled) == [1, 2]


def check_uniformity():
    nums = [1, 2, 3]
    counts = Counter()

    for seed in range(6000):
        gen = ListDistributionGenerator(nums, seed)
        shuffled = tuple(gen.fisher_yates())
        counts[shuffled] += 1

    print(counts)


################################
# TEST ALMOST SORTED:
################################
def test_almost_sorted_preserves_elements():
    nums = [5, 2, 4, 1, 3]
    gen = ListDistributionGenerator(nums, 42)

    result = gen.almost_sorted()

    assert len(result) == len(nums)
    assert sorted(result) == sorted(nums)


def test_almost_sorted_does_not_modify_original():
    nums = [5, 2, 4, 1, 3]
    gen = ListDistributionGenerator(nums, 42)

    _ = gen.almost_sorted()

    assert nums == [5, 2, 4, 1, 3]


def test_almost_sorted_same_seed_same_output():
    nums = [5, 2, 4, 1, 3]

    gen1 = ListDistributionGenerator(nums, 42)
    gen2 = ListDistributionGenerator(nums, 42)

    assert gen1.almost_sorted() == gen2.almost_sorted()


def test_almost_sorted_empty():
    gen = ListDistributionGenerator([], 42)
    assert gen.almost_sorted() == []


def test_almost_sorted_single_element():
    nums = [7]
    gen = ListDistributionGenerator(nums, 42)
    assert gen.almost_sorted() == nums == sorted(nums)


def test_almost_sorted_preserves_duplicates():
    nums = [3, 1, 3, 2, 2]
    gen = ListDistributionGenerator(nums, 42)

    result = gen.almost_sorted()

    assert sorted(result) == sorted(nums)


################################
# TEST TWO ALTERNATING RUNS:
################################

def test_two_alternating_runs_basic():
    nums = [5, 2, 4, 1, 3, 6]
    gen = ListDistributionGenerator(nums, 42)

    result = gen.two_alternating_runs()
    expected = sorted(nums)[::2] + sorted(nums)[1::2]

    assert result == expected


def test_two_alternating_runs_preserves_elements():
    nums = [5, 2, 4, 1, 3, 6]
    gen = ListDistributionGenerator(nums, 42)

    result = gen.two_alternating_runs()

    assert sorted(result) == sorted(nums)


def test_two_alternating_runs_does_not_modify_original():
    nums = [5, 2, 4, 1, 3, 6]
    gen = ListDistributionGenerator(nums, 42)

    _ = gen.two_alternating_runs()

    assert nums == [5, 2, 4, 1, 3, 6]


def test_two_alternating_runs_with_duplicates():
    nums = [3, 1, 3, 2, 2]
    gen = ListDistributionGenerator(nums, 42)

    result = gen.two_alternating_runs()

    assert sorted(result) == sorted(nums)


def test_two_alternating_runs_empty():
    gen = ListDistributionGenerator([], 42)
    assert gen.two_alternating_runs() == []


def test_two_alternating_runs_single():
    gen = ListDistributionGenerator([7], 42)
    assert gen.two_alternating_runs() == [7]


def test_two_alternating_runs_structure():
    nums = [1, 2, 3, 4, 5, 6]
    gen = ListDistributionGenerator(nums, 42)

    result = gen.two_alternating_runs()

    mid = (len(result) + 1) // 2
    first_run = result[:mid]
    second_run = result[mid:]

    assert first_run == sorted(first_run)
    assert second_run == sorted(second_run)
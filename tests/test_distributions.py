from src.analysis.distributions import (
    fisher_yates,
    almost_sorted,
    two_alternating_runs,
)

from collections import Counter

################################
# TEST FISHER-YATES:
################################
def test_fisher_yates_preserves_elements():
    shuffled = fisher_yates([5, 2, 4, 1, 3], 42)

    assert len(shuffled) == 5
    assert sorted(shuffled) == [1, 2, 3, 4, 5]


def test_fisher_yates_preserves_duplicates():
    nums = [3, 1, 3, 2, 2]
    shuffled = fisher_yates(nums, 42)

    assert len(shuffled) == len(nums)
    assert sorted(shuffled) == sorted(nums)


def test_fisher_yates_does_not_modify_original():
    nums = [5, 2, 4, 1, 3]

    shuffled = fisher_yates(nums, 42)

    assert nums == [5, 2, 4, 1, 3]
    assert shuffled is not nums


def test_fisher_yates_same_seed_same_output():
    nums = [5, 2, 4, 1, 3]

    shuffled1 = fisher_yates(nums, 42)
    shuffled2 = fisher_yates(nums, 42)

    assert shuffled1 == shuffled2


def test_fisher_yates_empty():
    assert fisher_yates([], 42) == []


def test_fisher_yates_single_element():
    assert fisher_yates([7], 42) == [7]


def test_fisher_yates_two_elements():
    shuffled = fisher_yates([1, 2], 42)
    assert sorted(shuffled) == [1, 2]


def check_uniformity():
    nums = [1, 2, 3]
    counts = Counter()

    for seed in range(6000):
        shuffled = tuple(fisher_yates(nums, seed))
        counts[shuffled] += 1

    print(counts)


################################
# TEST ALMOST SORTED:
################################
def test_almost_sorted_preserves_elements():
    nums = [5, 2, 4, 1, 3]

    result = almost_sorted(nums, 42)

    assert len(result) == len(nums)
    assert sorted(result) == sorted(nums)


def test_almost_sorted_does_not_modify_original():
    nums = [5, 2, 4, 1, 3]

    _ = almost_sorted(nums, 42)

    assert nums == [5, 2, 4, 1, 3]


def test_almost_sorted_same_seed_same_output():
    nums = [5, 2, 4, 1, 3]

    assert almost_sorted(nums, 42) == almost_sorted(nums, 42)


def test_almost_sorted_empty():
    assert almost_sorted([], 42) == []


def test_almost_sorted_single_element():
    nums = [7]

    assert almost_sorted(nums, 42) == nums == sorted(nums)


def test_almost_sorted_preserves_duplicates():
    nums = [3, 1, 3, 2, 2]

    result = almost_sorted(nums, 42)

    assert sorted(result) == sorted(nums)


################################
# TEST TWO ALTERNATING RUNS:
################################
def test_two_alternating_runs_basic():
    nums = [5, 2, 4, 1, 3, 6]

    result = two_alternating_runs(nums, 42)
    expected = sorted(nums)[::2] + sorted(nums)[1::2]

    assert result == expected


def test_two_alternating_runs_preserves_elements():
    nums = [5, 2, 4, 1, 3, 6]

    result = two_alternating_runs(nums, 42)

    assert sorted(result) == sorted(nums)


def test_two_alternating_runs_does_not_modify_original():
    nums = [5, 2, 4, 1, 3, 6]

    _ = two_alternating_runs(nums, 42)

    assert nums == [5, 2, 4, 1, 3, 6]


def test_two_alternating_runs_with_duplicates():
    nums = [3, 1, 3, 2, 2]

    result = two_alternating_runs(nums, 42)

    assert sorted(result) == sorted(nums)


def test_two_alternating_runs_empty():
    assert two_alternating_runs([], 42) == []


def test_two_alternating_runs_single():
    assert two_alternating_runs([7], 42) == [7]


def test_two_alternating_runs_structure():
    nums = [1, 2, 3, 4, 5, 6]

    result = two_alternating_runs(nums, 42)

    mid = (len(result) + 1) // 2
    first_run = result[:mid]
    second_run = result[mid:]

    assert first_run == sorted(first_run)
    assert second_run == sorted(second_run)
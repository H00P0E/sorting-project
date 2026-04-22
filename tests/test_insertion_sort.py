from src.sorting_algorithms.insertion_sort import insertion_sort

def test_insertion_sort():
    nums = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
    assert insertion_sort(nums) == 36
    assert nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
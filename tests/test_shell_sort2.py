from src.sorting_algorithms.shell_sort2 import shell_sort2

def test_shell_sort2():
    nums = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
    assert shell_sort2(nums) == 40
    assert nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
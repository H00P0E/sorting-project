from src.sorting_algorithms.shell_sort5 import shell_sort5

def test_shell_sort5():
    nums = [5, 2, 4, 1, 3, 11, 9, 8, 7, 6, 0, 10]
    assert shell_sort5(nums) == 29
    assert nums == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
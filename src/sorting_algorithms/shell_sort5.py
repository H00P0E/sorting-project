
def shell_sort5(nums: list[int]) -> int:
    num_comparisons = 0
    n = len(nums)

    if n <= 1:
        return 0
    
    gaps = []
    k = 1
    while (3 ** k - 1) // 2 < n:
        gap = (3 ** k - 1) // 2
        gaps.append(gap)
        k += 1

    for gap in reversed(gaps):
        for i in range(gap, n):
            j = i
            while j >= gap:
                num_comparisons += 1
                if nums[j] < nums[j-gap]:
                    nums[j-gap] = nums[j-gap] ^ nums[j]
                    nums[j] = nums[j-gap] ^ nums[j]
                    nums[j-gap] = nums[j-gap] ^ nums[j]
                    j -= gap
                else:
                    break
    
    return num_comparisons

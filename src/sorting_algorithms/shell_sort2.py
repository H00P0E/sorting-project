
def shell_sort2(nums: list[int]) -> int:
    num_comparisons = 0
    n = len(nums)

    if n <= 1:
        return 0
    
    gaps = []
    k = 1
    while (2 ** k) <= n:
        gap = 2 * (n // (2 ** (k + 1))) + 1
        if gap > 0 and gap not in gaps:
            gaps.append(gap)
        k += 1

    for gap in gaps:
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
    
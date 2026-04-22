
def shell_sort1(nums: list[int]) -> int:
    num_comparisons = 0
    n = len(nums)

    if n <= 1:
        return 0
    
    gap = n // 2

    while gap > 0:
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
        
        gap //= 2
    
    return num_comparisons
            
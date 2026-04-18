
def shell_sort4(nums: list[int]) -> int:
    num_comparisons = 0
    n = len(nums)

    if n <= 1:
        return 0
    
    # Set of all 2^p * 3^q
    gaps_set = set()
    twop = 1
    while twop < n:
        res = twop
        while res < n:
            gaps_set.add(res)
            res *= 3            # Increment q
        twop *= 2               # Increment p

    gaps =sorted(gaps_set, reverse=True)

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
    
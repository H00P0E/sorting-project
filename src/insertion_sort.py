
def insertion_sort(nums: list[int]) -> int:
    num_comparisons = 0
    n = len(nums)

    if n <= 1:
        return 0
    
    # O(n^2)
    for i in range(1, n):
        j  = i
        while j > 0:
            num_comparisons += 1
            if nums[j] < nums[j-1]:
                nums[j-1] = nums[j-1] ^ nums[j]
                nums[j] = nums[j-1] ^ nums[j]
                nums[j-1] = nums[j-1] ^ nums[j]
                j -= 1
            else:
                break
    
    return num_comparisons
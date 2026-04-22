
def tim_sort(nums: list[int]) -> int:
    num_comparisons = 0
    n = len(nums)

    if n <= 1:
        return 0

    stack: list[tuple[int, int]] = []
    runs = run_decomposition(nums)

    # main loop for TimSort
    for run in runs:
        # #1
        # No need to explicitly remove run from runs because going through all runs in for loop
        stack.append(run)

        while True:
            h = len(stack)

            r1 = stack[-1][1] if h >= 1 else None
            r2 = stack[-2][1] if h >= 2 else None
            r3 = stack[-3][1] if h >= 3 else None
            r4 = stack[-4][1] if h >= 4 else None

            # #2
            if h >= 3 and r1 > r3:
                num_comparisons += merge_at(nums, stack, h-3)
            
            # #3
            elif h >= 2 and r1 >= r2:
                num_comparisons += merge_at(nums, stack, h-2)
            
            # #4
            elif h >= 3 and (r1 + r2) >= r3:
                num_comparisons += merge_at(nums, stack, h-2)
            
            # #5
            elif h >= 4 and (r2 + r3) >= r4:
                num_comparisons += merge_at(nums, stack, h-2)
            
            else:
                break
    
    # Greedly colapse remaining pushed runs by merging top two runs on the stack
    while len(stack) > 1:
        num_comparisons += merge_at(nums, stack, len(stack) - 2)
        
    return num_comparisons      # I HATE WHITESPACE


# Helper Functions:

def run_decomposition(nums: list[int]) -> list[tuple[int, int]]:
    n = len(nums)
    runs: list[tuple[int, int]] = []                            # List of tuples with start and length
    i = 0

    while i < n:
        start = i

        if i == n - 1:
            runs.append((start, 1))                             # If i is the last element -> run of length 1
            break

        # Decreasing run
        if nums[i+1] < nums[i]:
            i += 1
            while i < (n-1) and nums[i+1] < nums[i]:
                i += 1
            
            end = i
            nums[start:end+1] = reversed(nums[start:end+1])      # Flip decreasing run so it is sorted in nondecreasing order
            runs.append((start, end - start + 1))
            i += 1
        # Nondecreasing run
        else:
            i += 1
            while i < (n-1) and nums[i+1] >= nums[i]:
                i += 1
            
            end = i
            runs.append((start, end - start + 1))
            i += 1
    
    return runs


def merge_at(nums: list[int], stack: list[tuple[int, int]], i: int) -> int:
    start1, len1 = stack[i]
    start2, len2 = stack[i+1]

    run1 = nums[start1:start1+len1]
    run2 = nums[start2:start2+len2]

    p1 = 0
    p2 = 0
    write = start1
    num_comparisons = 0

    while p1 < len1 and p2 < len2:
        num_comparisons += 1
        if run1[p1] <= run2[p2]:
            nums[write] = run1[p1]
            p1 += 1
        else:
            nums[write] = run2[p2]
            p2 += 1
        write += 1

    # One of runs could still have unprocessed elements if runs aren't same length
    while p1 < len1:
        nums[write] = run1[p1]
        p1 += 1
        write += 1
    
    while p2 < len2:
        nums[write] = run2[p2]
        p2 += 1
        write += 1
    
    # Update merged runs on stack
    stack[i] = (start1, len1 + len2)
    del stack[i+1]

    return num_comparisons
    
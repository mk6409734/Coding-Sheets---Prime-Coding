def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0

    for num in arr:
        max_ending_here = max_ending_here + num
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Output should be 6 (subarray: [4, -1, 2, 1])

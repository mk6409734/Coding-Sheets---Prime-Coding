def find_pair_with_sum(arr, target_sum):
    seen = set()  # Set to store the elements we've seen so far
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    
    return -1  # Return -1 if no pair is found

# Example usage:
arr = [1, 2, 3, 4, 5]
target_sum = 6
print(find_pair_with_sum(arr, target_sum))  # Output should be [2, 4] or [1, 5]

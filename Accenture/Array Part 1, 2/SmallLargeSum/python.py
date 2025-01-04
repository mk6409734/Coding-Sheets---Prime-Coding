def SmallLargeSum(arr):
    if len(arr) <= 3:
        return 0
    even = []
    odd = []
    for i in range(len(arr)):
        if i % 2 == 0:
            even.append(arr[i])
        else: 
            odd.append(arr[i])
            
        
    even.sort(reverse=True)        
    odd.sort(reverse=True)   
    
    if len(even) < 2 or len(odd) < 2:
        return 0
        
    second_even = even[1]
    second_odd = odd[1]
    
    return second_even + second_odd
    


# Sample Test Case 1 
print(SmallLargeSum([3, 2, 1, 7, 5, 4])) # Output: 7
# Sample Test Case 2 
print(SmallLargeSum([4, 0, 7, 9, 6, 4, 2])) # Output: 10

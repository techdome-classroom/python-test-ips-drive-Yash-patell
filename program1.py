from typing import List
def smallest_missing_positive_integer(nums: List[int]) -> int:
    n=len(nums)
    """
    Implement the function smallest_missing_positive_integer 
    using the provided smallest_missing_positive_integer function 
    to find the smallest missing positive integer in the given list.

    """

    
    i = 0
    while i < n:
        if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
   
    return n + 1







    



  


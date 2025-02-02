def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0 

    counter = 0  
    n = len(nums)

    for i in range(1, n): 
        if nums[i] != nums[counter]:
            counter += 1  
            nums[counter] = nums[i]  

    return counter + 1 

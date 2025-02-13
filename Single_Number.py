#brute force appraoch
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the list in-place
        
        for i in range(len(nums) - 1):  # Stop before the last element
            if nums[i] != nums[i + 1]:  # If the current element isn't the next one
                return nums[i]
        
        # If no number was returned in the loop, the last element must be the single one
        return nums[-1]

#hash variation
def single_number_hash(nums):
    num_counts = {}  # Dictionary to store counts

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1  # Count occurrences

    for num, count in num_counts.items():
        if count == 1:
            return num  # Return the unique number

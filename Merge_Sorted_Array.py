#brute force appraoch
nums1 = [1,2,3,0,0]
nums2 = [3,4,5,6]
nums1[len(nums1):] = nums2
print(nums1)
nums1.sort()
print(nums1)

#optimized approach
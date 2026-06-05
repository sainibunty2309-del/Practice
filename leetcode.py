#   DSA preperation Questions
# 
#  1. Two Sum
#  Link -> https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array
# 
# 


### Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.

# you can return the answer in any order.

"""class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []
"""

#### 217. Contains Duplicate
#### Link -> https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=array


"""class Solution(object):
    def containsDuplicate(self, nums):
     seen = set()

     for num in nums:
        if num in seen:
            return True
        seen.add(num)
     return False
"""

### 238. product of array excrpt self
# 
#### link ->https://leetcode.com/problems/product-of-array-except-self/?envType=problem-list-v2&envId=array


"""class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        ans =[1]*n
        prefix=1

        for i in range(n):
            ans[i]=prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(n-1,-1,-1):
            ans[i]*= postfix
            postfix *= nums[i]
        
        return ans
"""
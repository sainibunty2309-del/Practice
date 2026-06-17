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

# 1929. Concatenation of Array
# Link -> https://leetcode.com/problems/concatenation-of-array/submissions/2034185418/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

'''
Given an integer array nums of length n, you want to create an array ans 
of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

'''

# Solution :

'''
class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums
'''
# Shuffle the Array
# Link -> https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

'''
Given the array nums consisting of 2n elements
 in the form [x1,x2,...,xn,y1,y2,...,yn].
'''

# Solution :

'''
class Solution(object):
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])

        return ans
'''

# 485. Max Consecutives Ones
# Link -> https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

'''
Given a binary array nums, 
return the maximum number of consecutive 1's in the array.
'''

# Solution :

'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
      max_count = 0
      count = 0

      for num in nums:
          if num ==1:
             count +=1
             max_count = max(max_count, count)
          else:
             count = 0
      return max_count
'''

# 645. Set Mismatch
# Link -> https://leetcode.com/problems/set-mismatch/submissions/2035098386/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

'''
Find the number that occurs twice and the number that is 
missing and return them in the form of an array.
'''

# Solution :

'''
class Solution(object):
    def findErrorNums(self, nums):
      seen = set()
      duplicate = -1

      for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
      missing = -1
      n = len(nums)
      for i in range(1,n+1):
        if i not in seen:
            missing = i
            break
      
      return [duplicate, missing]
'''

# 1365. How many numbers are smaller than the current number
# Link -> https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

'''
Given the array nums, for each nums[i] find out how many numbers in the
array are smaller than it. That is, for each nums[i] you have to count 
the number of valid j's such that j != i and nums[j] < nums[i].

'''

# Solution:

'''
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count +=1
            ans.append(count)
        return ans
'''

# 448. Find all numbers disappeared in an array
# Link -> https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/2035117601/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

'''
Given an array nums of n integers where nums[i] is in the range
 [1, n], return an array of all the integers in the 
 [1, n] that do not appear in nums.
'''
# Solution:

'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        ans = []

        for i in range(1, len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans
'''

# 1441. Build an array with stack Operations
# Link -> https://leetcode.com/problems/build-an-array-with-stack-operations/submissions/2035130953/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

'''
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

- "Push": pushes an integer to the top of the stack.
- "Pop": removes the integer on the top of the stack.

You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack 
(from the bottom to the top) equal to target. You should follow the
 following rules:

- If the stream of the integers is not empty, pick the next 
integer from the stream and push it to the top of the stack.

- If the stack is not empty, pop the integer at the top of the stack.

If, at any moment, the elements in the stack (from the bottom to the top)
are equal to target, do not read new integers from the stream 
and do not do more operations on the stack.

Return the stack operations needed to build target following the 
mentioned rules. If there are multiple valid answers, 
return any of them.
'''

# Solution :

'''
class Solution(object):
    def buildArray(self, target, n):
        ans = []
        i = 0

        for num in range(1, n+1):
            if i == len(target):
                break

            ans.append("Push")

            if num == target[i]:
                i +=1
            else:
                ans.append("Pop")
        return ans
'''

# 636. Exclusive time of functions
#Link ->https://leetcode.com/problems/exclusive-time-of-functions/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

'''
A function's exclusive time is the sum of execution times for all 
function calls in the program. For example, if a function is called 
twice, one call executing for 2 time units and another call executing 
for 1 time unit, the exclusive time is 2 + 1 = 3.

'''

# Solution :

'''
class Solution(object):
    def exclusiveTime(self, n, logs):
        ans = [0]* n
        stack = []
        prev_time = 0

        for log in logs:
            parts = log.split(":")
            func_id = int(parts[0])
            action = parts[1]
            time = int(parts[2])

            if action == "start":
                if stack:
                    ans[stack[-1]] += time-prev_time
                stack.append(func_id)
                prev_time = time
            
            else:
                ans[stack.pop()] += time-prev_time +1
                prev_time = time +1
        return ans
        
'''

# 347. Top K frequented elements
# Link -> https://leetcode.com/problems/top-k-frequent-elements/submissions/2036399348/

'''
Given an integer array nums and an integer k, return the k 
most frequent elements. You may return the answer in any order.
'''

# Solution :

'''
class Solution(object):
    def topKFrequent(self, nums, k):
      d = {}

      for i in nums:
        if i in d:
            d[i] += 1
        else:
                d[i] = 1
        
      Ist = sorted(d.items(), key=lambda x: x[1], reverse = True)

      ans = []

      for item in Ist:
        ans.append(item[0])
        if len(ans) ==k:
            break

      return ans        
'''
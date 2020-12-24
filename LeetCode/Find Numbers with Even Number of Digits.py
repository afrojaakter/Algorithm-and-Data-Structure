'''
question: Given an array nums of integers, return how many of them contain an even number of digits.

example: 
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digits = 0
        for i in nums:
          disits = 0
            while i>0:
              i = i //10
              digits +=1
            if digits %2 == 0:
              even_digits += 1
          return even_digits

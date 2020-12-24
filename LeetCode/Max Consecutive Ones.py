#Question: Given a binary array, find the maximum number of consecutive 1s in this array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_ones = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_ones = 0
            else:
                count_ones += 1
                result = max(count_ones, result)
        return result
        

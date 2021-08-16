"""
Success
Details 
Runtime: 116 ms, faster than 79.12% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20 MB, less than 62.42% of Python3 online submissions for Contains Duplicate.
"""

#check if the nums array contains duplicated number
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
        
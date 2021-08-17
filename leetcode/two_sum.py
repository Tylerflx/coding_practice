"""
Success
Details 
Runtime: 52 ms, faster than 96.05% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 60.31% of Python3 online submissions for Two Sum.
"""
#O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find 2 number in the list that add up to be the same as target
        check_here = {}
        for i, num in enumerate(nums):
            if target - num in check_here:
                return [check_here[target - num], i] 
            check_here[num] = i
                
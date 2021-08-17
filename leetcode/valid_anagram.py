"""
Success
Details 
Runtime: 48 ms, faster than 68.07% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.9 MB, less than 27.35% of Python3 online submissions for Valid Anagram.
"""
#O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram should be word that have same length, same number of characters, same characters
        return  sorted(s) == sorted(t)
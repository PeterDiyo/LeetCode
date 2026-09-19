# LEETCODE 242: VALID ANAGRAM
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example: s = "anagram", t = "nagaram" -> Output: true, s = "rat", t = "car" -> Output: false.

"""
Sorting:
- Sort both strings and compare them. If they are equal, then t is an anagram of s.
- Time complexity: O(n log n + m log m) due to sorting.
"""
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
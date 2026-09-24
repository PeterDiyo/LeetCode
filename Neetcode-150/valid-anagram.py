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


"""
Hash Map:
- Count the frequency of each character in both strings and compare the counts.
- Time complexity: O(n + m) where n and m are the lengths of the strings.
- Space complexity: O(1) since we have atmost 26 characters (assuming only lowercase letters).
"""
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in range(len(s)):
        count_s[s[char]] = count_s.get(s[char], 0) + 1
        count_t[t[char]] = count_t.get(t[char], 0) + 1

    return count_s == count_t


"""
Hash Table (Using Array):
- Use an array of size 26 to count the frequency of each character in both strings.
- Time complexity: O(n + m) where n and m are the lengths of the strings.
- Space complexity: O(1) since we have at most 26 characters (assuming only lowercase letters).
"""
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True
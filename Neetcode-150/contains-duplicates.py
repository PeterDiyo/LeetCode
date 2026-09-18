# LEETCODE 217: CONTAINS DUPLICATES
# You are given an integer array nums. You need to check if any value appears at least twice in the array, and return true if any value appears at least twice in the array, and false if every element is distinct.
# Example: nums = [1,2,3,1] -> Output: true, nums = [1,2,3,4] -> Output: false.

"""
Brute force:
- Iterate through the array using two nested loops and check if any two elements are equal.
- Time complexity: O(n^2)
"""
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


"""
Sorting: 
- Sort the array and then check if any two adjacent elements are equal.
- Time complexity: O(n log n) due to sorting.
"""
def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
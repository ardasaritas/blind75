# Leetcode #15 Three Sum

from typing import List

class Solution:
    '''
    Solution for threeSum:
        Solution:
            Sort the list to use two pointer approach.
            For every num in list, search a pair where the sum of three is 0.

        Optimizations:
            First check if num > 0, if is positive, we possibly can not find a dublet that makes the sum 0, as the list is sorted.
            Check for redundant starting numbers, if i == 0 get the triplet(s) it provides once, than skip the rest.
            When a triplet is found, skip the redundant inners, if there are any, to not calculate same results for same numbers.

        Time Complexity:
            O(nlogn) for sorting
            O(n^2) for the algo itself,

            --> O(n^2)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            low = i + 1
            high = len(nums) - 1
            target = -num

            while low < high:
                if nums[low] + nums[high] < target:
                    low += 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    result.append([nums[low], nums[high], num])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1
        return result
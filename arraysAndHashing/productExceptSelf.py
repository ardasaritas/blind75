from math import floor, ceil
from typing import List

# Leetcode #238 Product of Array Except Self
class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Prefix
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Postfix
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result


if __name__ == "__main__":
    print(Solution.productExceptSelf([1,2,3,4 ]))

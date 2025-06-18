from typing import List

# LeetCode #217: Contains Duplicate
class Solution:
    @staticmethod
    def hasDupHashMap(nums: List[int]) -> bool:
        # Time: O(n), Space: O(n) - Hash map approach
        occurrences = {item: 0 for item in nums}
        for num in nums:
            if occurrences[num] < 2:
                occurrences[num] += 1
            if occurrences[num] == 2:
                return True
        return False

    @staticmethod
    def hasDupSorting(nums: List[int]) -> bool:
        # Time: O(n log n), Space: O(1) - Sort then check adjacent
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    @staticmethod
    def hasDupHashSet(nums: List[int]) -> bool:
        # Time: O(n), Space: O(n) - Hash set
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

    @staticmethod
    def hasDupHashLen(nums: List[int]) -> bool:
        # Time: O(n), Space: O(n) - Most efficient: compare lengths
        return len(set(nums)) < len(nums)

############################################################################################################

class Tester:
    def __init__(self):
        pass  # No instance needed since Solution methods are static
    
    def test_method(self, method_name: str, test_cases: List[tuple]):
        """
        Test a Solution method with multiple test cases
        method_name: name of the method to test (e.g., 'hasDupHashSet')
        test_cases: list of (input, expected_output) tuples
        """
        # Dynamically get method by string name from Solution class
        method = getattr(Solution, method_name)
        print(f"\nTesting {method_name}:")
        print("-" * 40)
        
        passed = 0
        total = len(test_cases)
        
        for i, (input_data, expected) in enumerate(test_cases, 1):
            try:
                result = method(input_data)
                status = "PASS" if result == expected else "FAIL"
                print(f"Test {i}: {status} - Input: {input_data}, Expected: {expected}, Got: {result}")
                if result == expected:
                    passed += 1
            except Exception as e:
                print(f"Test {i}: ERROR - Input: {input_data}, Error: {e}")
        
        print(f"\nResults: {passed}/{total} tests passed")
        return passed == total


# Example usage:
if __name__ == "__main__":
    tester = Tester()
    
    # Test cases: (input, expected_output)
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
        ([1, 2], False),
        ([2, 2], True)
    ]
    
    # Test all methods
    tester.test_method("hasDupHashMap", test_cases)
    tester.test_method("hasDupHashSet", test_cases)
    tester.test_method("hasDupSorting", test_cases)
    tester.test_method("hasDupHashLen", test_cases)
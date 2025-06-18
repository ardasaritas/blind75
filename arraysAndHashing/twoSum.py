from typing import List

# Leetcode #1: Two Sum
class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash map storage
        """
        map = dict()  # value -> index mapping
        for i, num in enumerate(nums):
            diff = target - num
            # Check if complement exists in our seen values
            if diff in map:
                return [map[diff], i]  # Return indices of the pair
            map[num] = i  # Store current number and its index
        
        return []  # No solution found (problem guarantees solution exists)

############################################################################################################

class Tester:
    def __init__(self):
        # Initialize the tester - no setup needed since Solution methods can be called statically
        pass
    
    def test_method(self, method_name: str, test_cases: list):
        """
        Generic method to test any Solution class method
        
        Args:
            method_name (str): Name of the method to test (e.g., 'twoSum')
            test_cases (list): List of tuples where each tuple contains:
                              (input_args, expected_output)
                              For twoSum: ((nums, target), expected_indices_list)
        """
        solution = Solution()
        method = getattr(solution, method_name)
        
        passed_tests = 0
        total_tests = len(test_cases)
        
        print(f"\n--- Testing {method_name} ---")
        
        for i, (inputs, expected) in enumerate(test_cases):
            try:
                # Unpack inputs and call the method
                if isinstance(inputs, tuple):
                    result = method(*inputs)
                else:
                    result = method(inputs)
                
                # For twoSum, we need to check if indices are valid and sum to target
                if method_name == "twoSum" and isinstance(inputs, tuple) and len(inputs) == 2:
                    nums, target = inputs
                    if (len(result) == 2 and 
                        0 <= result[0] < len(nums) and 
                        0 <= result[1] < len(nums) and
                        result[0] != result[1] and
                        nums[result[0]] + nums[result[1]] == target):
                        print(f"Test {i + 1}: PASSED - Input: {inputs}, Got indices: {result}, Values: [{nums[result[0]]}, {nums[result[1]]}]")
                        passed_tests += 1
                    else:
                        print(f"Test {i + 1}: FAILED - Input: {inputs}, Got: {result}")
                        if len(result) == 2:
                            print(f"  Sum check: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}, Expected: {target}")
                else:
                    # Generic comparison for other methods
                    if result == expected:
                        print(f"Test {i + 1}: PASSED - Input: {inputs}, Expected: {expected}, Got: {result}")
                        passed_tests += 1
                    else:
                        print(f"Test {i + 1}: FAILED - Input: {inputs}, Expected: {expected}, Got: {result}")
                        
            except Exception as e:
                print(f"Test {i + 1}: ERROR - Input: {inputs}, Exception: {str(e)}")
        
        # Print summary
        print(f"\nSummary: {passed_tests}/{total_tests} tests passed")
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        print(f"Success rate: {success_rate:.1f}%")
        
        return passed_tests == total_tests

if __name__ == "__main__":
    # Create tester instance
    tester = Tester()
    
    # Define test cases for twoSum method
    # Format: ((nums_list, target), expected_behavior_check)
    # Note: For twoSum, we validate the result rather than exact indices since multiple valid answers exist
    two_sum_test_cases = [
        # Basic cases
        (([2, 7, 11, 15], 9), "valid_indices"),     # Classic example: indices should sum to 9
        (([3, 2, 4], 6), "valid_indices"),          # Should return indices that sum to 6
        (([3, 3], 6), "valid_indices"),             # Duplicate values
        
        # Edge cases
        (([1, 2], 3), "valid_indices"),             # Minimum array size
        (([5, 5, 5, 5], 10), "valid_indices"),     # Multiple duplicates
        
        # Larger arrays
        (([1, 3, 7, 9, 2], 11), "valid_indices"),  # Should find 9 + 2 = 11
        (([1, 2, 3, 4, 5], 8), "valid_indices"),   # Should find 3 + 5 = 8
        
        # Negative numbers
        (([-1, -2, -3, -4, -5], -8), "valid_indices"),  # Should find -3 + -5 = -8
        (([1, -1, 0], 0), "valid_indices"),         # Should find 1 + -1 = 0
    ]
    
    # Run the tests
    print("Testing Two Sum Solution")
    print("=" * 40)
    
    all_passed = tester.test_method("twoSum", two_sum_test_cases)
    
    if all_passed:
        print("\n🎉 All tests passed!")
    else:
        print("\n⚠️  Some tests failed. Check the implementation.")
        print("\nNote: This tester validates that returned indices are valid")
        print("      and the values at those indices sum to the target.")
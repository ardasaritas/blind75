from typing import List, Any
from collections import Counter, defaultdict

# Leetcode #49 Group Anagrams

class Solution:

    # Strange enough, although mathematically neetcode's solution should be better. The sorting approach runs faster in
    # practical cases. Probably due to a tuple of 26 integers having much more collisions when hashing, and also the
    # the operation count each string goes through.
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together using sorted string as key.
        Time Complexity: O(m * n log n) where m = number of strings, n = max string length
        """
        if not strs:
            return []
        
        # Use defaultdict to group anagrams by their sorted key
        groups = defaultdict(list)
        
        for word in strs:
            # Create key by sorting characters - anagrams will have same key
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        # Return all groups as list of lists
        return list(groups.values())

    def groupAnagramsNeet(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together using alphabetic occurrences as key.
        Time Complexity: O(m * n) where m is number of strings, and n is the avg length of strings
        """

        res = defaultdict(list) # mapping character count to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return list(res.values())
############################################################################################################

class Tester:
    def __init__(self):
        # Initialize the tester - no setup needed since Solution methods can be called statically
        pass
    
    def test_method(self, method_name: str, test_cases: list):
        """
        Generic method to test any Solution class method
        
        Args:
            method_name (str): Name of the method to test (e.g., 'groupAnagrams')
            test_cases (list): List of tuples where each tuple contains:
                              (input_args, expected_output)
                              For groupAnagrams: (strs_list, expected_groups_list)
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
                
                # For groupAnagrams, we need to check if groups are equivalent
                # since order of groups and order within groups may vary
                if method_name == "groupAnagrams":
                    if self._are_anagram_groups_equal(result, expected):
                        print(f"Test {i + 1}: PASSED - Input: {inputs}")
                        print(f"  Result: {result}")
                        passed_tests += 1
                    else:
                        print(f"Test {i + 1}: FAILED - Input: {inputs}")
                        print(f"  Expected: {expected}")
                        print(f"  Got: {result}")
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
    
    def _are_anagram_groups_equal(self, result, expected):
        """
        Helper method to compare anagram groups regardless of order
        """
        if len(result) != len(expected):
            return False
        
        # Convert each group to sorted tuple for comparison
        result_normalized = {tuple(sorted(group)) for group in result}
        expected_normalized = {tuple(sorted(group)) for group in expected}
        
        return result_normalized == expected_normalized

if __name__ == "__main__":
    # Create tester instance
    tester = Tester()
    
    # Define test cases for groupAnagrams method
    # Format: (input_strings_list, expected_groups_list)
    group_anagrams_test_cases = [
        # Basic cases
        (["eat", "tea", "tan", "ate", "nat", "bat"], 
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        
        # Single string
        (["a"], [["a"]]),
        
        # Empty array
        ([], []),
        
        # All same anagrams
        (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),
        
        # No anagrams
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
        
        # Mixed cases
        (["listen", "silent", "hello", "world"], 
         [["listen", "silent"], ["hello"], ["world"]]),
        
        # Empty strings
        (["", ""], [["", ""]]),
        
        # Single characters
        (["a", "b", "a"], [["a", "a"], ["b"]]),
        
        # Longer strings
        (["anagram", "nagaram", "rat", "car"], 
         [["anagram", "nagaram"], ["rat"], ["car"]]),
    ]
    
    # Run the tests
    print("Testing Group Anagrams Solution")
    print("=" * 50)
    
    all_passed = tester.test_method("groupAnagrams", group_anagrams_test_cases)
    
    if all_passed:
        print("\n🎉 All tests passed!")
    else:
        print("\n⚠️  Some tests failed. Check the implementation.")
        print("\nNote: This tester compares anagram groups regardless of order")


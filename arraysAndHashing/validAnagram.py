from collections import Counter

# LeetCode #242: Valid Anagram
class Solution:
    @staticmethod
    def hasDuplicate(string: str) -> bool:
        """
        Helper function to check if a string contains duplicate characters.
        Uses set comparison for O(n) time complexity.
        """
        return len(set(string)) < len(string)

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        """
        Optimized solution that uses different approaches based on string characteristics:
        
        1. Early exit: If lengths differ, strings can't be anagrams
        2. Optimization: If either string has duplicates, use Counter for frequency comparison
        3. Simple case: If no duplicates, use set comparison (faster for unique chars)
        
        Time Complexity: O(n) where n is the length of strings
        """
        # Quick length check - anagrams must have same length
        # Time: O(1) - constant time operation
        if len(s) != len(t):
            return False
            
        # Check for duplicates in either string
        # Time: O(n) for each hasDuplicate() call due to set() creation
        if Solution.hasDuplicate(s) or Solution.hasDuplicate(t):
            # Counter creation: O(n) time
            # Counter comparison: O(k) time to compare hash tables where k is number of unique chars
            # Total: O(n) time
            return Counter(s) == Counter(t)
        else:
            # No duplicates means each char appears once - set comparison is sufficient
            # Set creation: O(n) time
            # Set comparison: O(min(len(set1), len(set2))) time
            # Total: O(n) time - faster than Counter for unique chars
            return set(s) == set(t)

############################################################################################################

class Tester:
    def __init__(self):
        # Initialize the tester - no setup needed since Solution methods can be called statically
        pass
    
    def test_method(self, method_name: str, test_cases: list):
        """
        Generic method to test any Solution class method
        
        Args:
            method_name (str): Name of the method to test (e.g., 'isAnagram')
            test_cases (list): List of tuples where each tuple contains:
                              (input_args, expected_output)
                              For isAnagram: ((s, t), expected_boolean)
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
                
                # Check if the result matches expected output
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
    
    # Define test cases for isAnagram method
    # Format: ((string1, string2), expected_boolean_result)
    anagram_test_cases = [
        # Basic anagram cases
        (("anagram", "nagaram"), True),    # Classic anagram example
        (("rat", "car"), False),           # Different characters
        (("listen", "silent"), True),      # Another classic anagram
        
        # Edge cases
        (("", ""), True),                  # Both empty strings
        (("a", "a"), True),                # Single identical characters
        (("a", "b"), False),               # Single different characters
        (("aacc", "ccac"), False),

        # Longer strings
        (("conversation", "voices rant on"), False),  # Contains space, should be False
        (("elbow", "below"), True),        # Valid anagram
    ]
    
    # Run the tests
    print("Testing Valid Anagram Solution")
    print("=" * 40)
    
    all_passed = tester.test_method("isAnagram", anagram_test_cases)
    
    if all_passed:
        print("\nAll tests passed!")
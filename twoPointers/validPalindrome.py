
# Leetcode #125 Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and keep only alphanumeric
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False
        return True


class PalindromeTester:
    def __init__(self):
        self.solution = Solution()
        self.test_cases = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            ("", True),
            ("a", True),
            ("Madam", True),
            ("No 'x' in Nixon", True),
            ("Mr. Owl ate my metal worm", True),
            ("1221", True),
            ("12321", True),
            ("hello", False),
            ("A Santa at NASA", True)
        ]
    
    def run_tests(self):
        passed = 0
        total = len(self.test_cases)
        
        for i, (input_str, expected) in enumerate(self.test_cases, 1):
            result = self.solution.isPalindrome(input_str)
            status = "✓" if result == expected else "✗"
            print(f"Test {i}: {status} '{input_str}' -> {result} (expected {expected})")
            if result == expected:
                passed += 1
        
        print(f"\nPassed: {passed}/{total}")
        return passed == total


if __name__ == "__main__":
    tester = PalindromeTester()
    tester.run_tests()

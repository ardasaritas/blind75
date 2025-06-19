import heapq
from typing import List
from collections import Counter, defaultdict

# Leetcode #347 Top K Frequent Elements

class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        """
        Find the k most frequent elements in an array using frequency inversion.
        
        Algorithm:
        1. Count frequency of each element using Counter
        2. Invert the mapping: frequency -> list of elements with that frequency
        3. Iteratively select from highest frequency buckets until k elements found

        Time Complexity: O(n + k * u) where n = len(nums), u = unique elements
        - O(n) to build frequency counter
        - O(u) to build inverted frequency map
        - O(k * u) for k iterations of finding max frequency

        """
        # Build frequency table: element -> count
        freq = Counter(nums)
        
        # Invert frequency mapping: count -> list of elements with that count
        # This allows us to efficiently find elements by their frequency
        inverted = defaultdict(list)
        for element, count in freq.items():
            inverted[count].append(element)

        result = []
        # Select k elements respecting frequency priority
        for i in range(k):
            # Find the highest remaining frequency
            max_freq = max(inverted.keys())
            
            # Get elements with this frequency and take the first one
            elements_with_max_freq = inverted[max_freq]
            result.append(elements_with_max_freq.pop(0))
            
            # Clean up empty frequency buckets to maintain accurate max finding
            if not elements_with_max_freq:
                del inverted[max_freq]

        return result

    @staticmethod
    def topKFrequentHeap(nums: List[int], k: int) -> List[int]:
        """
        Find k most frequent elements using heapq for optimal performance when k << n.
        
        Time Complexity: O(n log k) where n = len(nums)
        """
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)
    
    @staticmethod
    def topKFrequentSorted(nums: List[int], k: int) -> List[int]:
        """
        Find k most frequent elements by sorting all elements by their frequency.
        
        Time Complexity: O(n log n) where n = len(nums)
        """
        # Build frequency counter
        freq = Counter(nums)
        
        # Sort all unique elements by their frequency (descending order)
        # key=freq.get uses frequency as the sorting criterion
        sorted_by_freq = sorted(freq.keys(), key=freq.get, reverse=True)
        
        # Take first k elements from sorted list
        return sorted_by_freq[:k]
    
    @staticmethod
    def topKFrequentBuiltIn(nums: List[int], k: int) -> List[int]:
        """
        Find k most frequent elements using Counter's built-in most_common method.
        
        Time Complexity: O(n log n) - most_common() uses internal sorting
        """
        # Counter.most_common(k) returns list of (element, count) tuples
        # sorted by count in descending order
        most_common_pairs = Counter(nums).most_common(k)
        
        # Extract just the elements (first item of each tuple)
        return [element for element, count in most_common_pairs]

############################################################################################################

class Tester:
    def __init__(self):
        # Initialize the tester - no setup needed since Solution methods are static
        pass
    
    def test_method(self, method_name: str, test_cases: list):
        """
        Generic method to test any Solution class method
        
        Args:
            method_name (str): Name of the method to test (e.g., 'topKFrequent')
            test_cases (list): List of tuples where each tuple contains:
                              (input_args, expected_behavior)
                              For topKFrequent: ((nums, k), "valid_result")
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
                
                # For topKFrequent methods, validate the result correctness
                if "topKFrequent" in method_name and isinstance(inputs, tuple) and len(inputs) == 2:
                    nums, k = inputs
                    if self._is_valid_topk_result(nums, k, result):
                        print(f"Test {i + 1}: PASSED - Input: {inputs}, Result: {result}")
                        passed_tests += 1
                    else:
                        print(f"Test {i + 1}: FAILED - Input: {inputs}, Result: {result}")
                        print(f"  Validation failed: incorrect frequency ranking or count")
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
    
    def _is_valid_topk_result(self, nums, k, result):
        """
        Helper method to validate topKFrequent results
        """
        # Check basic constraints
        if len(result) != k:
            return False
        
        # Build frequency counter for validation
        freq = Counter(nums)
        
        # Check if all returned elements exist in original array
        for element in result:
            if element not in freq:
                return False
        
        # Check if result contains k most frequent elements
        # Get all elements sorted by frequency (descending)
        all_by_freq = sorted(freq.keys(), key=freq.get, reverse=True)
        expected_top_k = all_by_freq[:k]
        
        # Result should contain the same elements as expected (order may vary for ties)
        return set(result) == set(expected_top_k)
    
    def test_all_methods(self, test_cases: list):
        """
        Test all topKFrequent method variants with the same test cases
        """
        methods = [
            'topKFrequent',
            'topKFrequentHeap', 
            'topKFrequentSorted',
            'topKFrequentBuiltIn'
        ]
        
        print("Testing All TopK Frequent Methods")
        print("=" * 60)
        
        all_results = {}
        
        for method in methods:
            print(f"\n{'='*20} {method} {'='*20}")
            success = self.test_method(method, test_cases)
            all_results[method] = success
        
        # Summary
        print(f"\n{'='*60}")
        print("FINAL SUMMARY:")
        for method, success in all_results.items():
            status = "✅ PASSED" if success else "❌ FAILED"
            print(f"{method}: {status}")

if __name__ == "__main__":
    # Create tester instance
    tester = Tester()
    
    # Define test cases for topKFrequent methods
    # Format: ((nums, k), "valid_result") - we validate correctness rather than exact output
    topk_test_cases = [
        # Basic cases
        (([1, 1, 1, 2, 2, 3], 2), "valid_result"),        # Should return elements with freq 3,2
        (([1], 1), "valid_result"),                        # Single element
        (([1, 2], 2), "valid_result"),                     # All elements have same frequency
        
        # Edge cases
        (([4, 1, -1, 2, -1, 2, 3], 2), "valid_result"),   # Negative numbers
        (([1, 1, 2, 2, 3, 3], 3), "valid_result"),        # All elements have same frequency
        
        # Larger arrays
        (([1, 1, 1, 2, 2, 3, 4, 4, 4, 4], 2), "valid_result"),  # Clear frequency differences
        (([5, 5, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4], 3), "valid_result"),  # Multiple ties
        
        # Frequency ties
        (([1, 2, 3, 1, 2, 3], 2), "valid_result"),        # All have frequency 2
        (([1, 1, 2, 2, 3, 3, 4], 3), "valid_result"),     # Mixed frequencies
    ]
    
    # Test all methods
    tester.test_all_methods(topk_test_cases)
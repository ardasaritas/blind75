from typing import List


# Leetcode #271 Encode and Decode Strings
class Solution:

    @staticmethod
    def encode(strs: List[str]) -> str:
        """
        Encode list of strings into single string using format: "length#word"
        Example: ["hi", "hello"] → "2#hi5#hello"
        """
        result = ""
        for word in strs:
            # Add word length, delimiter, and word itself
            result += str(len(word)) + "#" + word
        return result

    @staticmethod
    def decode(s: str) -> List[str]:
        """
        Decode encoded string back to list of original strings
        Parses format: "length#word" for each encoded word
        """
        result = []
        i = 0  # Current position in encoded string
        
        # Process each encoded word until end of string
        while i < len(s):
            # Find delimiter to separate length from word
            delimiter_pos = s.find("#", i)
            
            # Read the length (number before #)
            length = int(s[i:delimiter_pos])
            
            # Extract the actual word using the length
            word_start = delimiter_pos + 1  # Skip the # delimiter
            word = s[word_start:word_start + length] # Get the word
            result.append(word)
            
            # Move to start of next encoded word
            i = word_start + length
            
        return result


if __name__ == "__main__":
    # This was the input I was having trouble on.
    print(Solution.decode(Solution.encode(["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"])))
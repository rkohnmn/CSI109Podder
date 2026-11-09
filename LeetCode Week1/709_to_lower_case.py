"""
LeetCode 709: To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"

Constraints:
1 <= s.length <= 100
s consists of printable ASCII characters.
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        # Convert the string to lowercase
        return s.lower()


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "Hello"
    result1 = solution.toLowerCase(s1)
    print("Example 1:")
    print(f"Input: s = \"{s1}\"")
    print(f"Output: \"{result1}\"")
    print()

    # Example 2
    s2 = "here"
    result2 = solution.toLowerCase(s2)
    print("Example 2:")
    print(f"Input: s = \"{s2}\"")
    print(f"Output: \"{result2}\"")
    print()

    # Example 3
    s3 = "LOVELY"
    result3 = solution.toLowerCase(s3)
    print("Example 3:")
    print(f"Input: s = \"{s3}\"")
    print(f"Output: \"{result3}\"")

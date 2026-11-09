"""
LeetCode 2235: Add Two Integers

Given two integers num1 and num2, return the sum of the two integers.

Example 1:
Input: num1 = 12, num2 = 5
Output: 17

Example 2:
Input: num1 = -10, num2 = 4
Output: -6

Constraints:
-100 <= num1, num2 <= 100
"""

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # Return the sum of the two integers
        return num1 + num2


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    num1, num2 = 12, 5
    result1 = solution.sum(num1, num2)
    print("Example 1:")
    print(f"Input: num1 = {num1}, num2 = {num2}")
    print(f"Output: {result1}")
    print()

    # Example 2
    num1, num2 = -10, 4
    result2 = solution.sum(num1, num2)
    print("Example 2:")
    print(f"Input: num1 = {num1}, num2 = {num2}")
    print(f"Output: {result2}")

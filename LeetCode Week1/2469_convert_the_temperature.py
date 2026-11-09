"""
LeetCode 2469: Convert the Temperature

You are given a non-negative floating point number rounded to two decimal places celsius, 
that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10^-5 of the actual answer will be accepted.

Formulas:
- Kelvin = Celsius + 273.15
- Fahrenheit = Celsius * 1.80 + 32.00

Example 1:
Input: celsius = 36.50
Output: [309.65000, 97.70000]

Example 2:
Input: celsius = 122.11
Output: [395.26000, 251.79800]

Constraints:
0 <= celsius <= 1000
"""

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        # Convert Celsius to Kelvin and Fahrenheit
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    celsius1 = 36.50
    result1 = solution.convertTemperature(celsius1)
    print("Example 1:")
    print(f"Input: celsius = {celsius1:.2f}")
    print(f"Output: [{result1[0]:.5f}, {result1[1]:.5f}]")
    print()

    # Example 2
    celsius2 = 122.11
    result2 = solution.convertTemperature(celsius2)
    print("Example 2:")
    print(f"Input: celsius = {celsius2:.2f}")
    print(f"Output: [{result2[0]:.5f}, {result2[1]:.5f}]")

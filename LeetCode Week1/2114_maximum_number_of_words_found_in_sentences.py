"""
LeetCode 2114: Maximum Number of Words Found in Sentences

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Example 1:
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence has 5 words.
- The second sentence has 4 words.
- The third sentence has 6 words.
Thus, the maximum number of words in a single sentence is 6.

Example 2:
Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3

Constraints:
1 <= sentences.length <= 100
1 <= sentences[i].length <= 100
sentences[i] consists only of lowercase English letters and ' ' only.
sentences[i] does not have leading or trailing spaces.
All the words in sentences[i] are separated by a single space.
"""

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0
        for sentence in sentences:
            # Count the number of words in the sentence
            word_count = len(sentence.split())
            if word_count > max_words:
                max_words = word_count
        return max_words


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    sentences1 = [
        "alice and bob love leetcode",
        "i think so too",
        "this is great thanks very much"
    ]
    result1 = solution.mostWordsFound(sentences1)
    print("Example 1:")
    print(f"Input: sentences = {sentences1}")
    print(f"Output: {result1}")
    print()

    # Example 2
    sentences2 = [
        "please wait",
        "continue to fight",
        "continue to win"
    ]
    result2 = solution.mostWordsFound(sentences2)
    print("Example 2:")
    print(f"Input: sentences = {sentences2}")
    print(f"Output: {result2}")

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Remove extra spaces and split into words
        words = s.split()

        # Step 2: Reverse the list of words
        reversed_words = words[::-1]

        # Step 3: Join the reversed words with a single space
        result = " ".join(reversed_words)

        return result

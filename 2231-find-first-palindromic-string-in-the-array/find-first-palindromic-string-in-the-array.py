class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        reversed1 = ''
        for i in range(len(words)):
            reversed1 = words[i][::-1]
            if reversed1 == words[i]:
                return reversed1
            reversed1 = ''
        return reversed1
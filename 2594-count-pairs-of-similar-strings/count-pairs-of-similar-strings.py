class Solution:
    def similarPairs(self, words: List[str]) -> int:
        char_count = {}
        count = 0
        for word in words:
            char = frozenset(word)

            if char in char_count:
                count += char_count[char]
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        return count
        


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        char_count = {}
        count = 0
        
        for word in words:
            char_set = frozenset(word)
            count += char_count.get(char_set, 0)
            char_count[char_set] = char_count.get(char_set, 0) + 1
        
        return count

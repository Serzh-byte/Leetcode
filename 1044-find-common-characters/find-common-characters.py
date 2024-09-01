from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        track = Counter(words[0])

        for word in words[1:]:
            check = Counter(word)
            for key in list(track.keys()): 
                if key in check:
                    if check[key] < track[key]:
                        track[key] = check[key]
                else:
                    track[key] = 0  
        
        result_list = [char for char, freq in track.items() for _ in range(freq) if freq > 0]
    
        return result_list

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index_dict = {value: index for index, value in enumerate(arr)}
        store = []
        
        for piece in pieces:
            if piece[0] not in arr:
                return False

            if len(piece) == 1 and piece[0] in index_dict:
                continue
            else:
                for i in range(len(piece) - 1):
                    char = piece[i]
                    next_char = piece[i + 1]
                    
                    if char not in index_dict or next_char not in index_dict:
                        return False
                    
                    first = index_dict[char]
                    second = index_dict[next_char]
                    
                    if second == first + 1:
                        store.append(first)
                    else:
                        return False
        
        return True

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        # If k == 0, all values should be 0
        if k == 0:
            return [0] * n
        
        # Create a result array to avoid modifying `code` in-place
        result = [0] * n
        
        for i in range(n):
            s = 0  # Reset sum for each `i`
            if k > 0:
                # Sum next `k` elements (circularly)
                for j in range(1, k + 1):
                    s += code[(i + j) % n]
            elif k < 0:
                # Sum previous `|k|` elements (circularly)
                for j in range(1, abs(k) + 1):
                    s += code[(i - j) % n]
            
            result[i] = s
        
        return result

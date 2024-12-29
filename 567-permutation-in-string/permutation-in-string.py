from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initialize pointers and Counters
        l, r = 0, len(s1) - 1
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])  # First window

        # Slide the window
        while r < len(s2):
            if s1_count == s2_count:  # Compare frequency counts
                return True
            
            # Update the window
            s2_count[s2[l]] -= 1  # Remove leftmost char
            if s2_count[s2[l]] == 0:  # Clean up zero counts
                del s2_count[s2[l]]
            l += 1  # Move left pointer
            
            r += 1  # Move right pointer
            if r < len(s2):  # Add new character to the window
                s2_count[s2[r]] += 1

        return False

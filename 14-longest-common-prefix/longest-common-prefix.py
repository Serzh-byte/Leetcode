class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # Start with the first string as the prefix
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:  
                    return ""
        
        return prefix

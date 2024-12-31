import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if cleaned_text[::-1] == cleaned_text:
            return True
        else:
            return False
        

        
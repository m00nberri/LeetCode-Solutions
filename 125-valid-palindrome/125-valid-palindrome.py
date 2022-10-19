class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = -1
        
        while l < len(s):
            if s[l].isalnum() == False:
                l += 1
            elif s[r].isalnum() == False:
                r -=1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(c.lower()for c in s if c.isalnum())
        n=len(s)
        i,j=0,n-1
        while j>=i:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        
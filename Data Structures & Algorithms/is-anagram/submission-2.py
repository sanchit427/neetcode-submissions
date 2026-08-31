class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numb={}
        for char in s:
            numb[char]=numb.get(char,0)+1
        for char in t :
            if char not in numb:
                return False
            numb[char]-=1
            if numb[char]==0:
                del numb[char]
        if len(numb)==0:
            return True
        else:
            return False
        
        

        
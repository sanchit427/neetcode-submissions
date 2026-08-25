class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        i=0
        ans=0
        freq={}
        for j in range(0,n):
            freq[s[j]]=freq.get(s[j],0)+1
            maxi = max(freq.values())
            replacement = (j - i + 1) - maxi
            if replacement > k:
                freq[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
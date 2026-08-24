class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seti = set()
        n = len(s)

        i, j = 0, 1
        seti.add(s[i])

        maxi = 1

        while j < n:
            if s[j] not in seti:
                seti.add(s[j])
                j += 1
                maxi = max(maxi, len(seti))
            else:
                seti.remove(s[i])
                i += 1

        return maxi
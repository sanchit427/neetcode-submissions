class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        n2 = len(s2)

        if n > n2:
            return False

        i = 0
        j = n - 1

        freq = {}
        freq2 = {}

        # Frequency of s1
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        # First window
        for k in range(i, j + 1):
            freq2[s2[k]] = freq2.get(s2[k], 0) + 1

        while j < n2:

            if freq == freq2:
                return True

           
            freq2[s2[i]] -= 1

            if freq2[s2[i]] == 0:
                del freq2[s2[i]]

           
            i += 1
            j += 1

            # Add new right character
            if j < n2:
                freq2[s2[j]] = freq2.get(s2[j], 0) + 1

        return False
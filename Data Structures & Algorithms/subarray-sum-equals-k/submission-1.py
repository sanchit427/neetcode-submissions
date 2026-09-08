from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        hashmap[0]=1
        total=0
        sumi=0
        for num in nums:
            sumi+=num
            prefix=sumi-k
            if prefix in hashmap:
                total += hashmap[prefix]
            hashmap[sumi] += 1
        return total


        
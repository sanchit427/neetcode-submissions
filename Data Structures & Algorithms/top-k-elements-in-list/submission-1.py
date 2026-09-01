from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicty = defaultdict(int)
        result = []
        
        for num in nums:
            dicty[num] += 1
        
        sorted_dicty = sorted(dicty.items(), key=lambda x: x[1], reverse=True)
        
        for k, v in sorted_dicty[:k]:  # only top k
            result.append(k)
        
        return result

        
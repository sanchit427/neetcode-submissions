from collections import defaultdict
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashi=defaultdict(int)
        result=[]
        for num in nums:
            hashi[num]+=1
        n=len(nums)
        target=math.floor(n/ 3)
        for key,value in hashi.items():
            if value >target:
                result.append(key)

        return result
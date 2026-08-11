class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequncy={}
        n=len(nums)
        maxi=-1
        for i in range(0,n):
            if nums[i] not in frequncy :
                frequncy[nums[i]]=1
            else:
                frequncy[nums[i]]+=1
        bucket=[[] for _ in range(n+1)]
        for nums,freq in frequncy.items():
            bucket[freq].append(nums)
        result = []
        for i in range(len(bucket) - 1, 0, -1):  
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
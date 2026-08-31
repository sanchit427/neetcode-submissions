class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        n=len(nums)
        for i in range(0,n):
            if target-nums[i] in x :
                result=[i,x[target-nums[i]]]
                result.sort()
                return result
            x[nums[i]]=i


               
        



        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate=set()
        n=len(nums)
        for i in range (0,n):
            if nums[i] not in duplicate:
                duplicate.add(nums[i])
            else:
                return True
        return False
            




        
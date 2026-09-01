class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sety = set(nums) 
        max_count = 0
        
        for num in nums:
            if num - 1 not in sety:
                count = 1
                while num + count in sety:
                    count += 1
                max_count = max(count, max_count)
        
        return max_count
        
        
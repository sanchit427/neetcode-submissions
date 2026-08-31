class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numb={}
        for num in nums:
            if num in numb:
                return True
            numb[num]=numb.get(num,0)+1
        return False

        
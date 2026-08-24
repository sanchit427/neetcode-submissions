class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        base_ans=(min(heights[0],heights[n-1])* (n-1))
        if heights[0]>heights[n-1]:
            j=n-2
            i=0
        else:
            i=1
            j=n-1
        while(j>i):
            ans=(min(heights[i],heights[j])* (j-i))
            if ans>base_ans:
                base_ans=ans
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return base_ans


        
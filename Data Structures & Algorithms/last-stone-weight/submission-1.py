class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap) > 1:
            stone1=-heapq.heappop(heap)
            stone2=-heapq.heappop(heap)
            if stone1>stone2:
                heapq.heappush(heap,-(stone1-stone2))
            elif stone2>stone1:
                heapq.heappush(heap,-(stone2-stone1))
        if heap:
            return -heap[0]
        return 0
        


        
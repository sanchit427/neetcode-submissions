import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        row=len(points)
        col=len(points[0])
        for point  in points:
                distance=  math.sqrt(point[0]**2 + point[1]**2)
                heapq.heappush(heap,(-distance,point))
                if len(heap)>k:
                    heapq.heappop(heap)
        return [point[1] for point in heap]
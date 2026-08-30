class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
    
    def findMedian(self) -> float:
        if len(self.arr)==0:
            return 0
        else:
            if len(self.arr)%2==0:
                self.arr.sort()
                middle1 = len(self.arr) // 2
                middle2 = len(self.arr) // 2 - 1
                median= (self.arr[middle1]+self.arr[middle2])/2
                return median
            else:
                self.arr.sort()
                median= len(self.arr) // 2
                return self.arr[median]



    
        
        
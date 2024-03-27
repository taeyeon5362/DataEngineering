class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        index = len(self.data) - 1
        
        while index != 1 :
            parentNode = index // 2
            print(parentNode)
            
            if self.data[parentNode] < self.data[index] :
                self.data[parentNode], self.data[index] = self.data[index], self.data[parentNode]
                index = parentNode
            else :
                break


def solution(x):
    return 0

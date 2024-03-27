class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        visitQueue = ArrayQueue()
        
        if self.root :  #빈 투리가 아니면 루트 노드가 있는 것, 큐에 루트 노드를 인큐함
            visitQueue.enqueue(self.root)
        
        while visitQueue.isEmpty() == False : #큐가 비어있지 않은 동안 반복해줌
            node = visitQueue.dequeue() #큐에서 꺼내서 node에 저장
            traversal.append(node.data) #꺼낸 노드를 방문 리스트에 저장
            
            if node.left : #노드에 왼쪽 자식 노드가 존재할 경우 저장
                visitQueue.enqueue(node.left)
            if node.right : #노드에 오른쪽 자식 노드가 존재할 경우 저장
                visitQueue.enqueue(node.right)
        return traversal
            


def solution(x):
    return 0

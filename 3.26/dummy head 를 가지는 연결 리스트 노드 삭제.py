class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next #삭제하려는 노드 담기
        
        if prev.next == None : #prev 다음에 노드가 없는 경우 삭제할 노드가 없기 때문에 None 리턴
            return None
        
        if curr.next == None : #삭제할 노드가 없는 경우
            if self.nodeCount == 1 : #유일 노드
                self.tail = None
            else : #유일 노드가 아닐 때
                self.tail = prev
        
        #링크 조정
        prev.next = curr.next
        self.nodeCount -= 1
        
        return curr.data
            

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount :
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


def solution(x):
    return 0

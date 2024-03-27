class Array Queue : #배열로 구현한 환형 큐
	def __init__ (self) :
            self.maxCount= n #빈 큐를 초기화 인자로 주어진 최대 큐 길이 설정
            self.data = [None] * n
            self.count = 0
            self.front = -1
            self.rear = -1
        def size(self) :
        	return self.count #현재 큐 길이 반환
        def isEmpty(self) :
            return self.count == 0 #큐가 비어 있는지 판단
        def isFull(self) :
        	return self.count == self.maxCount #큐가 꽉 차 있는지 판단
        def enqueue(self, x) :
            if self.isFull() :
            	#IndexError('Queue full') exception으로 처리
                raise IndexError('Queue empty')
            self.rear = (self.rear + 1) % self.maxCount
            self.data[self.rear] = x #큐에 데이터 원소 추가
            self.count += 1
        def dequeue(self) :
            if self.isEmpty() :
            	raise IndexError('Queue empty')
            self.front = (self.front + 1) % self.maxCount
            x = self.data[self.front]
            self.count -= 1
            return x #데이터 원소를 삭제(리턴)
        def peek(self) :
            if self.isEmpty() :
            	raise IndexError('Queue empty')
            return self.data[(self.front + 1) % self.maxCount] #큐의 맨 앞 원소 반환

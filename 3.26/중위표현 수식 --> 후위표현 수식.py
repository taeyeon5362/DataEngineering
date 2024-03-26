class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        if i in prec and opStack.isEmpty():
            opStack.push(i)
        elif i == '(' or (i in prec and prec[opStack.peek()] < prec[i]):
            opStack.push(i)
        elif i in prec and prec[opStack.peek()] >= prec[i]:
            while opStack.size() != 0 and prec[opStack.peek()] >= prec[i]:
                answer += opStack.pop()
            opStack.push(i)
        elif i == ')':
            while not opStack.isEmpty():
                if opStack.peek() == '(':
                    opStack.pop()
                    break
                answer += opStack.pop()
        else:
            answer += i
    for i in range (opStack.size()):
        answer += opStack.pop()   
    
    return answer

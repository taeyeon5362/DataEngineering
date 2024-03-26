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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        # 숫자인 경우 경우
        if type(token) is int:
            postfixList.append(token)
        # 닫는 괄호를 만나는 경우
        elif token == ")":
            #  여는 괄호를 만날 때까지 pop
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            # 스택에 있는 여는 괄호 pop
            opStack.pop()
        # 연산자인 경우
        else:
            # 스택이 비어있는 경우
            if opStack.isEmpty():
                opStack.push(token)
            # 스택에 연산자들이 있는 경우
            else:
                # 현재의 연산자의 우선 순위가 더 큰 경우 및 여는 괄호인 경우
                if prec[token] > prec[opStack.peek()] or token == "(":
                    opStack.push(token)
                # 현재의 연산자의 우선 순위가 더 작은 경우
                else:
                    # 스택에 있는 연산자들 중 현재의 연산자보다 우선 순위가 더 큰 경우 모두 pop
                    while not opStack.isEmpty():
                        if prec[token] <= prec[opStack.peek()]:
                            postfixList.append(opStack.pop())
                        else:
                            break
                    opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        else:
            b = valStack.pop()
            a = valStack.pop()
            if token == "*":
                valStack.push(a * b)
            elif token == "/":
                valStack.push(a / b)
            elif token == "+":
                valStack.push(a + b)
            elif token == "-":
                valStack.push(a - b)
    return valStack.pop()



def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

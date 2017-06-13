## B * C is Infix

## +A B is Prefix

## AB+ is Postfix


from stack import Stack

def infixToPostfix(infixexpr):
    prec ={}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()

    postfixList=[]

    tokenList=infixexpr.split()
    "( A + B ) * C - ( D - E ) * ( F + G )"
    ###operand [(] (
    ###postfix [A B +]
    for token in tokenList :
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token ==')':
            topToken = opStack.pop()
            while topToken !='(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())

            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ''.join(postfixList)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand2,operand1)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op,op2,op1):
    if op == '*':
        return op1*op2
    elif op == '/':
        return op1/op2
    elif op == "+":
        return op1 + op2
    else:
        return op1-op2

print(postfixEval('7 8 + 3 2 + /'))


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


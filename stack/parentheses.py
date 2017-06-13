from stack import HeadStack
def parChecker(symbolString):
    s=HeadStack()
    balanced = True
    index = 0
    #check whether parentheses is balanced or not

    while index < len(symbolString) and balanced :
        symbol = symbolString[index]
        #push opning parentheses
        if symbol == "(":
            s.push(symbol)
        else:
            #if there is no opening but closing is left in the String, unbalanced
            if s.isEmpty():
                balanced = False
            # or pop
            else:
                s.pop()
        # move to next
        index = index +1

    if balanced and s.isEmpty():
        return True
    else:
        return False

# check the order of multiple symbol by checking wether open and close are same same symbol

def parChecker2(symbolString):
    s = HeadStack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced :
        symbol = symbolString[index]

        if symbol in "([{" :
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# compare the index of open and close to make sure that they are same symbol
def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker2('{{([][])}()}'))
print(parChecker2('({[]})'))

# print(parChecker2('({[]})'))
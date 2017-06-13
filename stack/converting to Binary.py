from stack import Stack

def divideBy2(decNumber) :
    remstack = Stack()

    while decNumber >0 :
        rem = decNumber %2
        remstack.push(rem)
        decNumber = decNumber //2
    binString=''

    while not remstack.isEmpty():
        binString = binString +str(remstack.pop())

    return binString

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF" ## Set for digits over 9

    remstack = Stack()

    while decNumber >0:
        rem = decNumber %  base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''

    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()] ## pop the digit character for remainder


    return newString

print(baseConverter(25,2))

print(baseConverter(25,16))
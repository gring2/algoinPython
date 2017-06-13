def test(param):
    print(param)

    if param <=-1:
        return False
    test(param-1)
    print(param)



def test2(param):

    if param == 0:
        return True
    found = test2(param-1) or test2(param-2) or test2(param-3)

    if found:
        print("Fount!")
    return found


testArry =[1,2,3,4,5];

test =  [c for c in testArry if c <= 4]

print(test)

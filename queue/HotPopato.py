from Queue import Queue

def hotPotato(namelist, num) :
    simqueue = Queue()

    for name in namelist :
        simqueue.enqueue(name)
    while simqueue.size() > 1:

        for i in range(num) :
            print(simqueue.items)
            simqueue.enqueue(simqueue.dequeue())


        print(simqueue.items)
        simqueue.dequeue()
        print(simqueue.items)
    return simqueue.dequeue()


print(hotPotato(["Bill","David", "Susan", "Jane" , "Kent", "Brad"],7))


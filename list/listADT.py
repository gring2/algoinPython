class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found



    def remove(self, item):
        current = self.head
        previous =None
        found = False
        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        ## if First node is target
        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())



class OrderedList(UnorderedList):

    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            data = current.getData()
            print(data)
            if data == item:
                found = True

            else:
                if data > item:
                    print("STOP")
                    stop = True
                else:current = current.getNext()

        return found


orderdList = OrderedList()

orderdList.add(2)
orderdList.add(4)
orderdList.add(3)

orderdList.search(4)
class HashTable:
    def __init__(self):
        self.size = 11
        ##key
        self.slots = [None] * self.size
        ##value
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashfunction(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
            print(hashValue," ",self.slots," ", self.data)
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                ##슬롯이 차 있으면 반복해서 리해싱

                nextslot = self.rehash(hashValue,len(self.slots))
                while self.slots[nextslot] != None and \
                    self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data
                print("else ",hashValue, " ", self.slots, " ", self.data)

    def hashfunction(self,key,size):
        return key % size

    def rehash(self,oldhash,size):
        return (oldhash+1) % size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        ##키 배열에서 같은 키가 나오면 해당 해시 밸류로 데이터 찾음
        ##없으면 리 해싱
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)


H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

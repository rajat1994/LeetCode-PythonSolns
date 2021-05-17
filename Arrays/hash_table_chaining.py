class HashTable :
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]


    def get_hash(self, key):
        h = 0

        for char in key:
            h += ord(char)
        return h%self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break

        if not found :
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                break


ht = HashTable()

ht['march 6'] = 120
ht['march 6']= 78
ht['marhc 6'] = 234

print(ht.arr)

del ht['marhc 6']

print(ht.arr)
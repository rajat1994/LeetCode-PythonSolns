class HashTable :
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self, key):
        h = 0

        for char in key:
            h += ord(char)
        return h%self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


ht = HashTable()
ht['march 7'] = 10
ht['march 8'] = 20

print(ht['march 7'])
print(ht['march 8'])
print(ht.arr)
del ht['march 7']
print(ht.arr)

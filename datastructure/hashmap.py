# reference:
# http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html#lst-hashtablecodeconstructor

class HashTable(object):
    def __init__(self):
        self.size = 11
        # use two lists to create a HashTable
        self.keys = [None]*self.size
        self.data = [None]*self.size

    def hash(self, k, size):
        return k%size
    def has(self, string, size):
        ttl = 0
        for i in range(len(string)):
            ttl = ttl + ord(string[i])*i # *i for anagrams
        return ttl%size

    # open addressing (con: items easily become clustered in table)
    def rehash(self, k, size):
        return k%size + 1 # linear probing

    # rehasing, 3 must be a prime number as all the slots in the table will eventually be visited.
    def rehash(self, k, size):
        return (k+3)%size

    # quadratic probing
    def rehash(self, k, size):
        return k%size + 16 # h, h+1, h+4, h+9, h+16


    def put(self, k, d):
        hashval = self.hash(k, self.size)
        print "d = %s" % d

        if self.keys[hashval] == None:
            self.keys[hashval] = k
            self.data[hashval] = d
        else:
            if self.keys[hashval] == k:
                self.data[hashval] = d # replace
            else:
                newhashval = self.rehash(hashval, self.size)
                while self.keys[newhashval%self.size] != None \
                and self.keys[newhashval%self.size] != k:
                    print "hi"
                    newhashval = self.rehash(newhashval, self.size)
                if self.keys[newhashval%self.size] == None:
                    self.keys[newhashval%self.size] = k
                    self.data[newhashval%self.size] = d
                else:
                    self.data[newhashval%self.size] = d # replace

    def get(self, k):
        hashval = self.hash(k, self.size)
        print "hashval = %s" % hashval
        return self.data[hashval] if self.keys[hashval] is not None else -1

    def __setitem__(self,key,data):
        self.put(key,data)

    def __getitem__(self, key):
        self.get(key)


def main():
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print H.keys
    print H.data
    print H[20]

if __name__ == '__main__':
    main()
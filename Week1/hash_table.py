class HashTable:
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]

    def _hash(self, key):
        res = sum([ord(s) for s in key])
        print(res)
        return res % self.max_len

    def set(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        value = self.table[index]
        if not value:
            return None
        for v in value:
            if v[0] == key:
                return v[1]
        return None

if __name__ == "__main__":
    t = HashTable()

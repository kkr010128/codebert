class HashTable:
    def __init__(self, size = 1000003):
        self.size = size
        self.hash_table = [None] * size

    def _gen_key(self, val):
        raw_hash_val = hash(val)
        h1 = raw_hash_val % self.size
        h2 = 1 + (raw_hash_val % (self.size - 1))
        for i in range(self.size):
            candidate_key = (h1 + i * h2) % self.size
            if not self.hash_table[candidate_key] or self.hash_table[candidate_key] == val:
                return candidate_key

    def insert(self, val):
        key = self._gen_key(val)
        self.hash_table[key] = val

    def search(self, val):
        key = self._gen_key(val)
        if self.hash_table[key]:
            print('yes')
        else:
            print('no')


import sys

n = int(sys.stdin.readline())

simple_dict = HashTable()

ans = ''

for i in range(n):
    operation = sys.stdin.readline()
    if operation[0] == 'i':
        simple_dict.insert(operation[7:])
    else:
        simple_dict.search(operation[5:])
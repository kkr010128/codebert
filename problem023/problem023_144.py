class Dictionary:
    def __init__(self):
        self.elements = set()
    def insert(self, x):
        self.elements.add(x)
    def find(self, y):
        if y in self.elements:
            print('yes')
        else:
            print('no')

import sys

n = int(sys.stdin.readline())

simple_dict = Dictionary()

for i in range(n):
    operation = sys.stdin.readline()
    if operation[0] == 'i':
        simple_dict.insert(operation[7:])
    else:
        simple_dict.find(operation[5:])
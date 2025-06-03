class Dic:
    def __init__(self):
        self.end = False
        self.a = self.c = self.g = self.t = 0
    def insert(self, s):
        node = self
        index = 0
        while index < len(s):
            c = s[index]
            child = 0
            if c == 'A':
                if not node.a:
                    node.a = Dic()
                child = node.a
            elif c == 'C':
                if not node.c:
                    node.c = Dic()
                child = node.c
            elif c == 'G':
                if not node.g:
                    node.g = Dic()
                child = node.g
            elif c == 'T':
                if not node.t:
                    node.t = Dic()
                child = node.t
            else:
                return
            node = child
            index += 1
        node.end = True
    def find(self, s):
        node = self
        index = 0
        while index < len(s):
            c = s[index]
            child = 0
            if c == 'A':
                child = node.a
            elif c == 'C':
                child = node.c
            elif c == 'G':
                child = node.g
            elif c == 'T':
                child = node.t
            if child == 0:
                return False
            node = child
            index += 1
        return node.end

dic = Dic()

n = int(input())
for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'insert':
        dic.insert(cmd[1])
    elif cmd[0] == 'find':
        print('yes' if dic.find(cmd[1]) else 'no')


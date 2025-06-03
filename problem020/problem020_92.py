class DoublyLinkedList:
    def __init__(self):
        self.nil = self.make_node(None)
        self.nil['next'] = self.nil
        self.nil['prev'] = self.nil

    def make_node(self,v):
        return {'key':v, 'next':None, 'prev':None}

    def dump(self):
        n = self.nil['next']
        while True:
            if n['key'] == None:
                break
            else:
                print str(n['key']),
                n = n['next']
        print


    def insert(self,v):
        n = self.make_node(v)
        n['next'] = self.nil['next']
        self.nil['next']['prev'] = n
        n['prev'] = self.nil
        self.nil['next'] = n

    def delete(self,v):
        self.delete_node(self.list_search(v))

    def delete_node(self,n):
        if n['key'] == None: return
        n['next']['prev'] = n['prev']
        n['prev']['next'] = n['next']

    def list_search(self,v):
        cur = self.nil['next']
        while (cur['key'] != None) and (cur['key'] != v):
            cur = cur['next']
        return cur

    def deleteFirst(self):
        self.delete_node(self.nil['next'])

    def deleteLast(self):
        self.delete_node(self.nil['prev'])

n = int(raw_input())
commands = []
for i in range(n):
    commands.append(raw_input())

l = DoublyLinkedList()
for c in commands:
    a = c[6]
    if a == "F":
        l.deleteFirst()
    elif a == "L":
        l.deleteLast()
    else:
        val = int(c[7:])
        op = c[0]
        if op == "i":
            l.insert(val)
        else:
            l.delete(val)

l.dump()
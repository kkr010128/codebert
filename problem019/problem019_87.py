class Queue():
    def __init__(self):
        self.el = []
        
    def add(self, el):
        self.el.append(el)
        
    def delete(self):
        return self.el.pop(0)
    
    def action(self):
        self.el[0]['time'] -= q
        tmp = self.delete()
        self.el.append(tmp)

n, q = map(int, raw_input().split())
qu = Queue()

for i in range(n):
    name, time = raw_input().split()
    time = int(time)
    qu.add({'name':name, 'time':time})

time = 0
while qu.el:
    #print qu.el
    if qu.el[0]['time'] > q:
        qu.action()
        time += q
    else:
        time += qu.el[0]['time']
        print qu.el[0]['name'], time
        qu.delete()
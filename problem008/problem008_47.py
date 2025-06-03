from collections import OrderedDict

class Stack():
    def __init__(self):
        self.el = []
    def add(self, el):
        self.el.append(el)
    def pop(self):
        return self.el.pop()
    def top(self):
        return self.el[-1]
    def isEmpty(self):
        if self.el:
            return False
        return True

class Node():
    def __init__(self, id, edge=[], flag=0, discover=0, finish=0):
        self.id = id
        self.edge = edge
        self.flag = flag
        self.discover = discover
        self.finish = finish
    def show(self):
        print self.id, self.discover, self.finish
        
def notVisited(dic):
    for i in dic.keys():
        if dic[i].flag != 2:
            return i
    return None
        
n = int(raw_input())
dic = {}
for i in range(n):
    tmp = map(int, raw_input().split())
    if tmp[1] > 0:
        dic[tmp[0]] = Node(tmp[0], tmp[2:])
    else:
        dic[tmp[0]] = Node(tmp[0])
dic = OrderedDict(dic)

start = 1
time = 1
st = Stack()
dic[start].flag = 1
dic[start].discover = time
st.add(dic[start])

while not st.isEmpty():
    time += 1
    u = st.top()
    v = u.edge
    if v:
        for i in range(len(v)):
            if dic[v[i]].flag == 0:
                dic[v[i]].flag = 1
                dic[v[i]].discover = time
                if i != len(v)-1:
                    dic[u.id].edge = u.edge[i+1:]
                else:
                    dic[u.id].edge = []
                st.add(dic[v[i]])
                break
        else:
            st.pop()
            dic[u.id].flag = 2
            dic[u.id].finish = time
    else:
        st.pop()    
        dic[u.id].flag = 2
        dic[u.id].finish = time
    if st.isEmpty() and notVisited(dic):
        new = notVisited(dic)
        dic[new].flag = 1
        time += 1
        dic[new].discover = time
        st.add(dic[new])
for i in dic.keys():
    dic[i].show()
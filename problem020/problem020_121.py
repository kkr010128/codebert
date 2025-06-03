import sys
res = dict()
dll = [None] * 2000000
left = 0
right = 0
n = int(input())
for inpt in sys.stdin.read().splitlines():
    i = inpt.split()
    if i[0] == "insert":
        x = int(i[1])
        dll[left] = x
        if(x in res):
            res[x].add(left)
        else:
            res[x] = set([left])
        left += 1
    if i[0] == "delete":
        x = int(i[1])
        if(x in res):
            ind = max(res[x])
            dll[ind] = None
            res[x].remove(ind)
            if(len(res[x]) == 0):
                del res[x]
            if(ind == (left - 1)):
                left = ind
            if(ind == right):
                right += 1
    if i[0] == "deleteFirst":
        left -= 1
        x = dll[left]
        res[x].remove(left)
        if(len(res[x]) == 0):
            del res[x]
        dll[left] = None
    if i[0] == "deleteLast":
        right += 1
    # print(dll[right:left])
ret = []
for x in dll[right:left]:
    if(x is not None):
        ret.append(str(x))
ret.reverse()
print(" ".join(ret))
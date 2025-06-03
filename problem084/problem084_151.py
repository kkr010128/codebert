N,M = tuple(map(int,input().split()))
# matchlist = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(M)]
#最大のグループの大きさを出す
friendlist = list(range(N))
# [所属先,[所属メンバー]]
gplist = [[i] for i in range(N)]

def getgroup(a):
    A = friendlist[a]
    if A == a:
        return a
    else:
        return getgroup(A)

def match(ab):
    A = getgroup(ab[0])
    B = getgroup(ab[1])
    if A==B:
        return
    elif len(gplist[A])<len(gplist[B]):
        gplist[B].extend(gplist[A])
        friendlist[A] = B
    else:
        gplist[A].extend(gplist[B])
        friendlist[B] = A

for i in range(M):
    # print(friendlist)
    # print(gplist)
    match(tuple(map(lambda x:int(x)-1,input().split())))

# print(friendlist)
# print(gplist)

print(max([len(item) for item in gplist]))
T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split()) #高橋君
B1,B2 = map(int,input().split()) #青木君

# 時間配列
T = [T1]
f = 1
for i in range(3):
    if f:
        Tn = T2
        f = 0
    else:
        Tn = T1
        f = 1
    T.append(T[-1]+Tn)
# print(T)

class runner():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
        
    def distance(self,t):
        d = t//(T1+T2)*(self.v1*T1 + self.v2*T2)
        tm = t % (T1+T2)
        # print("d",d,"tm",tm)
        if tm < T1:
            d += self.v1 * tm
        else:
            d += self.v2*(tm-T1) + self.v1*T1
        return d

dif = runner(A1-B1,A2-B2)

c = -1
D = 0
DL = [0]
for t in T:
    pD = D
    D = dif.distance(t)
    DL.append(D)
    # print(D)
    if pD*D <= 0:
        c += 1
# print(c)
# print(DL)

if DL[1]*DL[2] > 0:
    print(0)
else:
    if DL[2] == 0:
        print("infinity")
    else:
        a = DL[2]
        if a>0:
            if -DL[1]%a == 0:
                print(-DL[1]//a*2)
            else:
                print(-DL[1]//a*2+1)
        else:
            if -DL[1]%a == 0:
                print(-DL[1]//a*2)
            else:
                print(-DL[1]//a*2+1)
H1,M1,H2,M2,K = (int(x) for x in input().split())
Wake  = 60*H1+M1
Sleep = 60*H2+M2

Activate = Sleep - Wake
CanStudy = Activate - K
print(int(CanStudy))
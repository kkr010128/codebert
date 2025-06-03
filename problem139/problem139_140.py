H1,M1,H2,M2,K = map(int,input().split())

h = H2 - H1
m = M2 - M1
s = 0

s = h * 60 + m


s = s - K

print(s)
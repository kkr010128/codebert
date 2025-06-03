S,H,C,D = set(),set(),set(),set()
W = set([1,2,3,4,5,6,7,8,9,10,11,12,13])
n = int(input())
for i in range(n):
    N = input().split()
    if N[0] == 'S':
        S.add(int(N[1]))
    elif N[0] == 'H':
        H.add(int(N[1]))
    elif N[0] == 'C':
        C.add(int(N[1]))
    elif N[0] == 'D':
        D.add(int(N[1]))
s,h,c,d = [],[],[],[]
st = W - S
while st != set():
  s.append(st.pop())
s.sort()
ht = W - H
ct = W - C
dt = W - D
while ht != set():
  h.append(ht.pop())
h.sort()
while ct != set():
  c.append(ct.pop())
c.sort()
while dt != set():
  d.append(dt.pop())
d.sort()

for i in s:
    print('S {0}'.format(i))
for i in h:
    print('H {0}'.format(i))
for i in c:
    print('C {0}'.format(i))
for i in d:
    print('D {0}'.format(i))
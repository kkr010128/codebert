n = int(input())
s = input()
x = [int(i) for i in s]
pc = s.count('1')

def popcnt(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

def f(x):
    if x == 0:
        return 0
    return f(x % popcnt(x)) + 1

ans = [0]*n
for a in range(2):
    npc = pc
    if a == 0:
        npc += 1
    else:
        npc -= 1
    
    if npc <= 0:
        continue
    
    r0 = 0
    for i in range(n):
        r0 = (r0*2) % npc
        r0 += x[i]

    k = 1
    for i in range(n-1, -1, -1):
        if x[i] == a:
            r = r0
            if a == 0:
                r = (r+k) % npc
            else:
                r = (r-k+npc) % npc
            ans[i] = f(r) + 1
        k = (k*2) % npc

for i in ans:
    print(i)
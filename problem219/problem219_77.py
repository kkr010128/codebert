N = list(input())
M = [ int(i) for i in N[::-1] ]
M.append(0)
c = 0

for i in range(len(M)-1):
    if M[i] >= 6 or ( M[i] >=5 and M[i+1] >= 5):
        M[i+1] += 1
    c += min(M[i],10-M[i])
c += M[len(M)-1]

print(c)
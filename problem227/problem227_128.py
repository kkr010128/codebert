n,k = map(int, input().split()) 
h = [int(x) for x in input().split()]

if n<=k:
    print(0)
    exit()

h.sort()

print(sum(h[:n-k]))
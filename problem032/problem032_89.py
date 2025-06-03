n = int(input())
x, y = [list(map(float,input().split()))for i in range(2)]
print("%.6f"%sum([abs(x[i]-y[i])for i in range(n)]))
print("%.6f"%pow(sum([abs(x[i]-y[i])**2 for i in range(n)]), 1/2))
print("%.6f"%pow(sum([abs(x[i]-y[i])**3 for i in range(n)]), 1/3))
print(*max([abs(x[i]-y[i])] for i in range(n)))


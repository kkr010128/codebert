n = int(input())
x = []

for i in range(n):
    a, b = map(int, input().split())
    x.append([a, b])
    
ans = 0
for i in range(len(x) - 1):
    for j in range(i+1, len(x)):
        ans += ((x[i][0]-x[j][0])**2 + (x[i][1]-x[j][1])**2)**0.5
        
print((2*ans)/n)
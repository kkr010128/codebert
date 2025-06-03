n = int(input())
ans = 0
for i in range(1,n+1):
    min = i
    max = int(n/i)*i
    xx = (max-min)/i+1
    ans += xx*(max+min)/2

print(int(ans))
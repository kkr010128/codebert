n = int(input())

def cal(i):
    s = (i + i*(n//i))*(n//i)*0.5
    return s

ans = 0
for i in range(1, n+1):
    ans += cal(i)
    
print(int(ans))

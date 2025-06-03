"""
全探索
"""
n = int(input())
for i in range(1,10) :
    if n % i == 0 and 0 <= n//i <= 9 :
        print("Yes")
        break
else :
    print("No")

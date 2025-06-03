lines = int(input())
mini = int(input())
maxi = -1000000000
for i in range(1,lines):
    s = int(input())
    maxi = max(maxi,s - mini)
    mini = min(s,mini)
print(maxi)
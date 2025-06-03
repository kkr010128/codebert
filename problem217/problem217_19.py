n = int(input())
q = list(map(int,input().split()))
ans = 0
count = 0
for i in q:
    if i%2 == 0:
        alm = i
        count += 1
        if alm%3 == 0 or alm%5 == 0:
            ans += 1
if ans == count:
    print("APPROVED")
else:
    print("DENIED")
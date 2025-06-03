n = int(input())
l = list(map(int,input().split()))+[0]
l.sort(reverse=True)
ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        left = j
        right = n
        while right - left > 1:
            middle = (left + right)//2
            if l[i]-l[j] < l[middle]:
                left = middle
            else:
                right = middle
        ans += (left-j)
print(ans)
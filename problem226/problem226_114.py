h, n = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort(reverse=True)

max_point = sum(A[:n])
ans = 'Yes'
if max_point < h:
    ans = 'No'
    
print(ans)
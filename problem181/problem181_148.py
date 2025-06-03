import collections 
K = int(input())

l = collections.deque([1,2,3,4,5,6,7,8,9])

cnt = 0
while True:
    n = l.popleft()
    cnt +=1
    if cnt ==K:
        print(n)
        exit()

    if n%10 != 0:
        l.append(10*n+n%10-1)

    l.append(10*n+n%10)

    if n%10 != 9:
        l.append(10*n+n%10+1)
    

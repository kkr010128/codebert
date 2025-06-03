import collections

K = int(input())

L = [1,2,3,4,5,6,7,8,9]
Q = collections.deque(L)
count = 0 

while count < K-1:
    V = Q.popleft()
    count+=1
    if V%10 == 0:
        Q.append(10*V)
        Q.append(10*V+1)
    elif V%10 == 9:
        Q.append(10*V+8)
        Q.append(10*V+9)
    else:
        Q.append(10*V+(V%10)-1)
        Q.append(10*V+(V%10))
        Q.append(10*V+(V%10)+1)

print(Q.popleft())
#B
N = int(input())

a = [i+1 for i in range(N)]

a_sub=[]
for i in a:
    if i%15 != 0 and i%5 !=0 and i%3 !=0:
        a_sub.append(i)
print(sum(a_sub))
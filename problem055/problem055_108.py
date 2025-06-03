n = int(input())
li = ["#"*20 if i%4==0 else "0"*10 for i in range(1, 16)]
for _ in range(n):
    b, f, r, v = map(int, input().split())
    h = 4*b-(4-f)-1
    li[h] = li[h].replace(li[h], ''.join([str(int(list(li[h])[r-1])+v) if i == r-1 else list(li[h])[i] for i in range(10)]))
li = [' '+' '.join(li[i]) if (i+1)%4!=0 else li[i] for i in range(len(li))]
print('\n'.join(li))

n = int(input())
list_a = [i for i in range(1,n+1) if i % 3 ==0]
list_b = []
for i in range (1,n+1):
    j = i
    while True:
        if j == 0:
            break
        elif j % 10 == 3:
            list_b.append(i)
            break
        j = j // 10
    
a = set(list_a)
b = set(list_b)
c =list(a | b)
c.sort()
print(" " + " ".join(map(str,c)))
s2 = list(input()*2)
p = list(input())
for i in range(len(s2)-len(p)):
    a = [ s2[i+j] for j in range(len(p))]
    if a == p:
        print("Yes")
        break
else:
    print("No")
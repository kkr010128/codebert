m={"S":[], "D":[], "H":[], "C":[]}
for i in range(int(input())):
    mark, num=input().split()
    m[mark].append(int(num))
for j in ["S", "H", "C", "D"]:
    nai=set(range(1,14))-set(m[j])
    for k in nai:
        print(j, k)
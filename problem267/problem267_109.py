N=int(input())
s=input()

count=0

for i in range(0,10):
    if str(i) in s[:-2]:
        index_1=s.index(str(i))

        for j in range(0,10):
            if str(j) in s[index_1+1:-1]:
                index_2=s[index_1+1:-1].index(str(j))+index_1+1

                for k in range(0,10):
                    if str(k) in s[index_2+1:]:
                        count+=1
print(count)

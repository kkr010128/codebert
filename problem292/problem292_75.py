n=int(input())
list=list(map(int, input().split()))
def pair(parameter):
        pairedList = []
        for iterater1 in range(len(parameter)):
                for iterater2 in range(iterater1+1,len(parameter)):
                        pairedList.append([parameter[iterater1],parameter[iterater2]])
        return pairedList

pairings = pair(list)
count=0
add=0
for i in pairings:
    x=i[0]*i[1]
    add+=x
print(add)

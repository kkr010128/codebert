elements = input()
vector_1 = list(map(float,input().split()))
vector_2 = list(map(float,input().split()))

for i in range(1,4):
    minkowski = sum([abs(a-b)**i for (a,b) in zip(vector_1,vector_2)])**(1/i)
    print("{0:.7f}".format(minkowski))

minkowski_inf=max([abs(a-b) for (a,b) in zip(vector_1,vector_2)])
print("{0:.7f}".format(minkowski_inf))
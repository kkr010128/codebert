ans=[]
while True:
    a=input()

    if '?' in a:
        break

    eval('ans.append(int({0}))'.format(a))

for a in ans:
    print(a)

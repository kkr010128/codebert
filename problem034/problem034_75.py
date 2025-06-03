def rotate(arr,i):
    if i=='W':
        arr=[arr[k-1] for k in [3,2,6,1,5,4]]
    if i=='E':
        arr=[arr[k-1] for k in [4,2,1,6,5,3]]
    if i=='N':
        arr=[arr[k-1] for k in [2,6,3,4,1,5]]
    if i=='S':
        arr=[arr[k-1] for k in [5,1,3,4,6,2]]
    return arr
arr=input().split()

deck=[]
for i in 'W'*4:
    arr=rotate(arr,i)
    for k in 'NNNN':
        arr=rotate(arr,k)
        deck.append(arr)
arr=rotate(arr,'N')
arr=rotate(arr,'W')
for k in 'NNNN':
    arr=rotate(arr,k)
    deck.append(arr)
arr=rotate(arr,'W')
arr=rotate(arr,'W')
for k in 'NNNN':
    arr=rotate(arr,k)
    deck.append(arr)
n=int(input())
for i in range(n):
    query=input().split()
    for v in deck:
        if v[0]==query[0] and v[1]==query[1]:
            print(v[2])
            break


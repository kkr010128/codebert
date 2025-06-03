def solver(arr):
    stool = 0
    for i in range(1, len(arr)):
        
        if arr[i]<arr[i-1]:
            stool += -arr[i]+arr[i-1]
            arr[i] = arr[i-1]
    return stool


if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(solver(arr))
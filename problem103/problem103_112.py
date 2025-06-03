n= int(input())
arr = [int(x) for x in input().strip().split()]


def Greedy(arr):
    
    curr = 1000
    for i in range(len(arr)-1):
        if arr[i+1]>arr[i]:
            stocks = curr // arr[i]
            curr += (arr[i+1] - arr[i])*stocks
    return curr

print(Greedy(arr))

_=input()
arr=list(map(int, input().split()))
odd=[n for (n,y) in enumerate(arr,1) if n%2 > 0 and y%2 > 0]
print (len(odd))
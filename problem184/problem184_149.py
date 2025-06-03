arr=list(input())
if len(arr)<6:print("No")
else:
    if arr[2]==arr[3] and arr[4]==arr[5]:
        print("Yes")
    else: print("No")
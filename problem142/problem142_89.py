N = input().rstrip()
N = int(N[-1])
A = {2,4,5,7,9}
B = {0,1,6,8}
if N in A:
    print("hon")
elif N in B:
    print("pon")
else:
    print("bon")
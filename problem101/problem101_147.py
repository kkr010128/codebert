A, B, C = [int(v) for v in input().strip().split(" ")]
K = int(input().strip())

while K > 0:
    if B <= A:
        B *= 2
        K -= 1
    elif C <= B:
        C *= 2
        K -= 1
    else:
        break

if C > B > A:
    print("Yes")
else:
    print("No")
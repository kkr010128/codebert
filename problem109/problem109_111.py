N = int(input())
ans = [0]*4
for i in range(N):
    s = input()
    if s == "AC":
        ans[0] += 1
    elif s == "WA":
        ans[1] += 1
    elif s == "TLE":
        ans[2] += 1
    elif s == "RE":
        ans[3] += 1
print("AC x "+ str(ans[0]),"WA x "+ str(ans[1]),"TLE x "+ str(ans[2]),"RE x "+ str(ans[3]),sep = "\n" )
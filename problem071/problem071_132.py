def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())


s=input()
if s[-1]=="s":
    print(s+"es")
else:
    print(s+"s")
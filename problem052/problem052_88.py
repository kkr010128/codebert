n = int(input())
result = ""
for s in range(1, n+1):
    if s % 3 == 0:
        result += " "+str(s)
    else:
        for i in str(s):
            if i == "3":
                result += " "+str(s)
                break
print(result)
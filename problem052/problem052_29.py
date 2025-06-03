n = int(input())
result = []
for i in range(1,n+1):
    si = str(i)
    if (not i % 3) or "3" in si:
        result.append(si)
print(" " + " ".join(result))
n = int(input())
sumOfN = sum(int(i) for i in list(str(n)))
print("No" if sumOfN%9 else "Yes")
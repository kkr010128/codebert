a,b,c = [int(i) for i in input().split()]
print("Yes" if(a * a + b * b + c * c - 2 * a * b - 2 * b * c - 2 * c * a > 0 and c - a - b > 0) else "No")
a = input().split()
b = input().split()
t = input()

dist = abs(int(a[0])-int(b[0]))
len = int(int(a[1]) - int(b[1]))*int(t)

if (dist > len):
	print("NO")
else:
	print("YES")
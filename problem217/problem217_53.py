n = int(input())
m = map(int, input().split())
flag = "APPROVED"

for i in m:
	if i % 2 == 0:
		if i % 3 != 0 and i % 5 != 0:
			flag = "DENIED"
    
print(flag)

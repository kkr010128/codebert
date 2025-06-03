x = int(input())
n = input()
t = "ABC"
c = 0;
for i in range(x-2):
	if n[i] == 'A' and n[i+1] =='B' and n[i+2] == 'C':
		c+=1
print(c)

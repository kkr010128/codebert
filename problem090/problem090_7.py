s = input()
 
ans = 0
for i in range(0, 3):
	if s[i] == 'R':
			ans += 1
      
if ans == 2 and s[1] == 'S':
  	ans -= 1
    
print(ans)
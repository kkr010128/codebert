x , y = map(int , input().split());
ans = 0;
if(x == 1):
	ans += 300000;
if(x == 2):
	ans += 200000;
if(x == 3):
  	ans += 100000;
if(y == 1):
	ans += 300000;
if(y == 2):
	ans += 200000;
if(y == 3):
  	ans += 100000;
if(x + y == 2):
  	ans += 400000;
print(ans)
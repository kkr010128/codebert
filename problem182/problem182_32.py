n, k, c = map(int, input().split())
s = str(input())
for i in range(n):
	if s[i] == 'o':
		ant = i+1
		antlist = [ant]
		break

for i in range(n):
	if s[n-i-1] == 'o':
		post = n-i
		postlist = [post]
		break

for i in range(k-1):
	ant += c+1
	post -= c+1
	for i in range(n):
		if s[ant+i-1] == 'o':
			ant += i
			antlist.append(ant)
			break
	for i in range(n):
		if s[post-i-1] == 'o':
			post -= i
			postlist.append(post)
			break
postlist.reverse()
#print(antlist)
#print(postlist)
for i in range(k):
	if antlist[i] == postlist[i]:
		print(antlist[i])
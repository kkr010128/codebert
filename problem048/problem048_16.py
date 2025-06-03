n = int(input())
i = 0

l = list(map(int, input().split()))
Max = l[0]
Min = l[0]
sum = 0
for i in range(0,n):
	sum += l[i]
	a = l[i]#変数の値が下の行の処理で変わってしまうのでaとかにしておく
	if a > Max:
		a,Max = Max,a
	if  a < Min:
		a,Min = Min,a
	
	
print(f"{Min} {Max} {sum}")
	

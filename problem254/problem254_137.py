A = int(input())
B = int(input())
AB = [A,B]
Ans = [x for x in range(1,4) if x not in AB]
print(Ans[0])
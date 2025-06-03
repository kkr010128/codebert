a, b = map(int, input().split())
tmp_a = int((a / 0.08) // 1)
tmp_b = int((b / 0.10) // 1)
check = True
# print(tmp_a, tmp_b)
for i in range(min(tmp_a,tmp_b), max(tmp_a + 1, tmp_b + 1) + 1):
    if int((i * 0.08)//1) == a and int((i * 0.10)//1) == b:
        print(i)
        check = False
        break
if check:
    print(-1)
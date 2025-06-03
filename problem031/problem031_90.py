std_value = []
while True:
    n = int(input())
    if n == 0:
        break
    s = [int(i) for i in input().split()]#生徒の点数
    sum_value=0
    s_ave = 0
    for i in range(len(s)):#平均値計算
        sum_value += s[i]
    ave = sum_value/len(s)
    for j in range(len(s)):
        s_ave += (s[j]-ave)**2
    std_value.append((s_ave/len(s))**(1/2))
for k in range(len(std_value)):
    print("{:.8f}".format(std_value[k]))

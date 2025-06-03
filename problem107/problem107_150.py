N = int(input())
X = input()

pop_X = sum(map(int,list(X)))
X_10 = int('0b'+X,2)

r_0 = X_10%(pop_X+1)
diff_0 = 1%(pop_X+1)

zero_flag = False
if pop_X == 1:
    zero_flag = True
else:
    r_1 = X_10%(pop_X-1)
    diff_1 = 1%(pop_X-1)

answer = []


for i in range(N)[::-1]:
    if X[i]=='0':
        r = (r_0+diff_0)%(pop_X+1)
    else:
        if zero_flag:
            answer.append(0)
            diff_0 = (diff_0*2)%(pop_X+1)
            continue
        else:
            r = (r_1-diff_1)%(pop_X-1)
    count = 1
    while True:
        if r == 0:
            break
        pop = sum(map(int,list(bin(r)[2:])))
        r = r % pop
        count += 1
        
    answer.append(count)
    diff_0 = (diff_0*2)%(pop_X+1)
    if zero_flag:
        continue
    diff_1 = (diff_1*2)%(pop_X-1)

for i in answer[::-1]:
    print(i)
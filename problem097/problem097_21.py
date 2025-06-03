K = int(input())
seven_number = 0
ality = 0
for ans in range(1,10**7):
        if ans > K:
            print("-1")
            break
        else:
            seven_number = (seven_number*10+7) % K
            if seven_number ==0:
                print(ans)
                break

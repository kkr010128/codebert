def FizzBuzz_sum():
    # 入力
    N = int(input())
    # 初期処理
    N = [i for i in range(1,N+1)]
    sum = 0
    # 比較処理
    for i in N:
        if i % 3 == 0 and i % 5 == 0:
            pass
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            sum += i
    return sum

result = FizzBuzz_sum()
print(result)
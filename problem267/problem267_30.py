import itertools

def my_index(l, x):
    if x in l:
        return l.index(x)
    else:
        return -1


if __name__ == "__main__":
        
    N = int(input())
    S = [int(c) for c in input()]
    table = list(range(10))

    count = 0
    for p in itertools.product(table, repeat=3): # 重複を許して1~9の数値を３つならべる
        target = list(p)

        s1_index = my_index(S, target[0])
        if s1_index == -1:
            continue
        s1 = S[s1_index+1:]

        s2_index = my_index(s1, target[1])
        if s2_index == -1:
            continue
        s2 = s1[s2_index+1:]
        
        s3_index = my_index(s2, target[2])
        if s3_index == -1:
            continue
        
        count += 1

    print(count)


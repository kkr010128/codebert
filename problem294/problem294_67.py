N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
total = 0

for i in range(N-2):
    a = L[i]
    for j in range(i+1, N-1):
        b = L[j]
        # j以降の項で、初めてL[k] < a-bとなるkを二分探索する
        if L[-1] > a - b:  # 一番最後の項でもOKな場合(j+1以降全部OK)
            total += N - j - 1
        elif L[j+1] <= a - b:  # 一番最初の項からNGな場合
            continue
        else:
            head = j+1  # head はL[head] > a - bを満たす(OK側)
            tail = N-1  # tail はL[tail] <= a - bを満たす(NG側)
            while head+1 != tail:
                if L[(head + tail)//2] > a - b:  # 中間地点はOK側
                    head = (head + tail) // 2
                else:  # 中間地点はNG側
                    tail = (head + tail) // 2
            total += head - j

print(total)

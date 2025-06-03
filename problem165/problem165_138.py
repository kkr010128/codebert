N = int(input())
#リスト内包表記
Ss = [input() for _ in range(N)]
Ss_set = set(Ss)
print(len(Ss_set))
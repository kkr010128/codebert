n,m = map(int,input().split())
# 受け取った文字をスペースで分けてリスト化
a = list(input().split())
# 文字列のリストの値を整数化
a_int = [int(i) for i in a]
# 夏休みの日数がリスト内の日数の合計より多ければ残日数を表示 
if n >= sum(a_int):
    print(n - sum(a_int))
# リスト内の日数の合計が夏休みの日数より多ければ-1を表示
else:
    print("-1")
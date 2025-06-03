def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    H,W,M = LMIIS()
    targets_row = []
    targets_column = []
    targets = []
    for i in range(M):
        column,row = LMIIS()
        targets_row.append(row)
        targets_column.append(column)
        targets.append((column,row))

    common_columns = Counter(targets_column).most_common()
    common_rows = Counter(targets_row).most_common()
    max_columns = defaultdict(bool)
    num_max_column = common_columns[0][1]
    for k,v in common_columns:
        if v < num_max_column:
            break
        max_columns[k] = True
    max_rows = defaultdict(bool)
    num_max_row = common_rows[0][1]
    for k,v in common_rows:
        if v < num_max_row:
            break
        max_rows[k] = True
    dbg(max_columns)
    dbg(max_rows)
    num_candidates = len(max_columns)*len(max_rows)
    

    num_target_on_intersection = 0
    for column, row in targets:
        if max_columns[column] and max_rows[row]:
            num_target_on_intersection += 1
    
    ans = common_columns[0][1] + common_rows[0][1]
    dbg(num_target_on_intersection)
    dbg(num_candidates)
    print(ans if num_target_on_intersection < num_candidates else ans - 1)
    

    
    
    

    
main()
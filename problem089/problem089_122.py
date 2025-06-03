def main():
    h, w, m = map(int, input().split())
    mapa = {}
    strings = [0]*h
    rows = [0]*w
    for _ in range(m):
        h1, w1 = map(int, input().split())
        if not mapa.get(h1-1, 0):
            mapa[h1-1] = []
        mapa[h1-1].append(w1-1)
        strings[h1-1] += 1
        rows[w1-1] += 1
    
    max_s = max(strings)
    max_r = max(rows)
    strings_max = []
    rows_max = []
    for i in range(h):
        if strings[i] == max_s:
            strings_max.append(i)
    for i in range(w):
        if rows[i] == max_r:
            rows_max.append(i)
    
    forbidden_positions = set(mapa[strings_max[0]])
    for item in strings_max[1:]:
        forbidden_positions.intersection_update(set(mapa[item]))

    answer_set = set(rows_max).difference(forbidden_positions)
    if answer_set:
        print(max_s + max_r)
    else:
        print(max_s + max_r - 1)

main()

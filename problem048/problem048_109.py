n = int(raw_input())
ai_list = map(int, raw_input().split())

max_ai = max(ai_list)
min_ai = min(ai_list)
sum_ai = sum(ai_list)

print '%d %d %d' % (min_ai, max_ai, sum_ai)
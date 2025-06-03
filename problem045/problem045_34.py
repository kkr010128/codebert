
val = map(int, raw_input().split())

ans1 = val[0] / val[1]
ans2 = val[0] % val[1]
ans3 = format(val[0] / float(val[1]), '.5f')

print("{} {} {}".format(ans1, ans2, ans3))
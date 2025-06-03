def main():
    inside_rate, outside_rate = map(int, input().split())
    correction = 0
    if inside_rate < 10:
        correction = 100 * (10 - inside_rate)
    print(outside_rate + correction)
main()
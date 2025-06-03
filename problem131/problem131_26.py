def main():
    a, v = map(int, input().split())
    b, w =map(int, input().split())
    t = int(input())

    distance = abs(b-a)
    speed = v-w
    if distance > speed*t:
        print('NO')
    else:
        print('YES')

main()
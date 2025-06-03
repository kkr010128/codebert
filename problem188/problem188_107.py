x, y, a, b, c = map(int, input().split())

red = list(map(int, input().split()))
green = list(map(int, input().split()))
colorless = list(map(int, input().split()))

red.sort(reverse = True)
green.sort(reverse = True)
colorless.sort(reverse = True)

ret = red[:x] + green[:y]
ret.sort()

for i in range(len(colorless)):
    if ret[i] < colorless[i]:
        ret[i] = colorless[i]
    else:
        break

print(sum(ret))
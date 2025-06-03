import sys

try:
    #d = int(input('D: '))
    #t = int(input('T: '))
    #s = int(input('S: '))
    nums = [int(e) for e in input().split()]
except ValueError:
    print('エラー：整数以外を入力しないでください')
    sys.exit(1)

if 1 <= nums[0] <= 10000 and 1 <= nums[1] <= 10000 and 1 <= nums[2] <= 10000:
    take_time = nums[0] / nums[2]
    if take_time <= nums[1]:
        print("Yes")
    else:
        print("No")
else:
    print('エラー：各入力は1～10000までの整数です')
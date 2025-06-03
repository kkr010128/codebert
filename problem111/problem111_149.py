n = input()
friendliness = [int(item) for item in input().split()]
friendliness.sort()
def of_ans():
    sum_ = 0
    idx = 1
    while idx < len(friendliness):
        sum_ += friendliness[len(friendliness) - (idx // 2) - 1]
        idx += 1
    return sum_
print(of_ans())
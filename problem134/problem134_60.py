# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)  # 配列を昇順ソートしておく(配列に0がある場合0が先頭に来るので、場合分けの必要がなくなる)
    ans = 1
    for val in arr:
        ans *= val  # Pythonは多倍長整数をサポートしているので単に積を求めれば十分
        if ans > 10 ** 18:
            print(-1)
            break
    else:
        print(ans)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

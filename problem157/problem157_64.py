import sys
import math
sys.setrecursionlimit(10**9)

def main():
    N = int(input())
    A = list(map(int,input().split()))

    dic = [{},{}]
    counted = [set(),set()]

    def count(x,type):
        type = type - 1
        if x <= 0:
            return

        if not x in counted[type]:
            dic[type][x] = 1
            counted[type].add(x)
        else:
            dic[type][x] += 1


    for i in range(N):
        type1 = (i+1)-A[i]
        type2 = (i+1)+A[i]

        count(type1,1)
        count(type2,2)

    ans = 0
    # print(dic,counted)
    for index,cnt in dic[0].items():
        if index in counted[1]:
            ans += cnt * dic[1][index]


    print(ans)



if __name__ == "__main__":
  main()
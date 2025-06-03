K = int(input())
A, B = map(int, input().split())
print("NOGK"[-(-A//K)*K <= B::2])
n = int(input())
txt = input()

print(txt[:n]+"..." if bool(txt[n:]) else txt)
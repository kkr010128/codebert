a = input()
al=[chr(ord('a') + i) for i in range(26)]
if a in al:
    print("a")
else:
    print("A")
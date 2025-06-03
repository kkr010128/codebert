n=int(input())
a=[input() for i in range(n)]
b=a.count("AC")
c=a.count("TLE")
d=a.count("WA")
e=a.count("RE")
print(f"AC x {b}")
print(f"WA x {d}")
print(f"TLE x {c}")
print(f"RE x {e}")



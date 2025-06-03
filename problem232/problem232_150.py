a,b = input().split()
aa,bb = int(a),int(b)
print(a * bb if a * bb < b * aa else b * aa)
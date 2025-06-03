a=map(int, raw_input().split())

if (min(a)<a[0]<max(a)):
    print min(a),a[0],max(a)
elif (min(a)<a[1]<max(a)):
    print min(a),a[1],max(a) 
else:
    print min(a),a[2],max(a) 
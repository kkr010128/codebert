import sys
s1=raw_input()
s2=raw_input()

def check(s1_top, s1, s2):
    for s2_idx, c in enumerate(s2):
        if c != s1[(s1_top + s2_idx) % len(s1)]:
            return False
    return True

l=[]    
for i, c in enumerate(s1):
    if c == s2[0]:
        if check(i, s1, s2):
            print "Yes"
            sys.exit(0)

print "No"
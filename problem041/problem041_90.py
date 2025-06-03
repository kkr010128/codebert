inl=map(int, raw_input().split())

if inl[0]>=inl[2]+inl[4] and inl[2]-inl[4]>=0 and inl[1]>=inl[3]+inl[4] and inl[3]-inl[4]>=0:
  print "Yes"
else:
  print "No"
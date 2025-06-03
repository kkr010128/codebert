# coding: utf-8

line = raw_input()
print ''.join([((s.lower() if s.isupper() else s.upper()) if s.isalpha() else s) for s in line])
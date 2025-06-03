# -*- coding: utf-8 -*-

def judge(m, f, r):
	if m==-1 or f==-1: return "F"
	
	ttl = m + f
	if ttl >= 80: return "A"
	elif ttl >= 65: return "B"
	elif ttl >= 50: return "C"
	elif ttl >= 30:
		return "C" if r>=50 else "D"
	else: return "F"

if __name__ == "__main__":
	while True:
		m, f, r = map(int, raw_input().split())
		if m==-1 and f==-1 and r==-1: break
		print judge(m, f, r)
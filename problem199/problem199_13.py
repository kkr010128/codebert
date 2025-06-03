class Solution(object):
	def is_hitachi_string(self, string):

		if len(string) == 0:
			print 'No'
			return

		hi_str = 'hi'
		hi_idx = 0
		for idx in xrange(len(string)):
			if idx > 9:
				print 'No'
				return

			if string[idx] != hi_str[hi_idx]:
				print 'No'
				return

			hi_idx = (hi_idx + 1) % 2

		if hi_idx == 0:
			print 'Yes'
		else:
			print 'No'

if __name__ == '__main__':
	sol = Solution()
	string = raw_input()
	sol.is_hitachi_string(string)
#coding:utf-8
'''
给定一个字符串，找到 s 当中最长的回文子串

比如：
input:'babad'
output: bab or aba

比如：
input:'cbbd'
output:'bb'

思路：
回文是以某个字符为中心的，但是如果是偶数的回文，比如abba的时候，其中心是bb中间的虚拟字符
'''
import time

class Solution:

	def expandAroundCenter(self,s,l,r):
		# 这是扩展函数,l,r就是以当前中心向左右两个方向进行扩展的
		while(l >= 0 and r < len(s) and s[l] == s[r]):
			#这个条件就是以中心左右是相等，那就是回文,然后继续看下一位是不是也想等
			l -=1
			r +=1
		return (r - max(l,0) - 1)  # 这是这个回文的长度

	def longestPalindrome(self,s):
		if len(s) == 0 or s == None:
			return ''
		end,start = 0,0
		for i in range(len(s)):
			# 这是第一层循环，这就是中心
			len1 = self.expandAroundCenter(s,i,i)      # 这是奇数回文，以当前点为中心
			len2 = self.expandAroundCenter(s,i,i+1)    # 这是偶数回文，以当前点和下一个点的中间为中心
			len_max = max(len1,len2)                  # 这是当前这个点得到的最长的回文
			if (len_max > (end - start)):
				start = max(0,i-(len_max-1)/2)
				#print(i,len_max,start,end)
				end = i + len_max/2
		return s[start:end+1]

	'''
	第二种解法：
	找到所有的回文的开始位置和最后的位置，然后验证该子串是不是回文
	这样，开始位置和最后的位置的配对种数就是 Cn2,这种解法就是消耗时间
	'''
	def Cn2(self,s):
		if len(s.strip()) == 0 or s == None:
			return ''
		if (len(s) == 1):
			#要有这个判断是因为s[:]的形式无法读取到s[0:0]
			return s
		ans = ''
		for i in range(len(s)):
			for j in range(i+1,len(s)+1):
				if s[i:j] == s[i:j][::-1]:
					ans = s[i:j] if len(s[i:j]) > len(ans) else ans
		return ans

	'''
	第三种解法：这种解法是上一种暴力解法的优化
	z这种解法是建立在，所有的回文都是单个字符回文以及两个字符回文的基础上的。即使说，回文中间的那个字符或者那两个字符一定要是回文才可以，因此，可以做两个循环
	每个循环，以单个回文为基础，然后去找该回文的扩展是不是回文，这就像是上面的中心扩展了
	'''

solution = Solution()
s = '0'*1000
start = time.time()
#print(solution.longestPalindrome(s))
print(solution.Cn2(s))
print(time.time()-start)





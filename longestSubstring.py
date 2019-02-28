# coding:utf-8
'''
问题是这样的，假设有一个字符串，需要做的是计算这个字符串中最大长度的无重复子串的长度
比如：
输入：‘abcabcbb'，则最长的无重复子串是 abc ，所以返回是3
输入:'bbbbb' ，则最长的无重复子串是 b,所以返回是1
输入：’pwwkew'最长的子串则是 wke
'''
class Solution:
	def lengthOfLongestSubstring(self,s):
		st = {} #这个是用来存储每个位置的子串的长度的字典
		i,ans = 0,0  # ans 是用来存储当前最大的字符串的长度的
		for j in range(len(s)):
			# 这里是根据 s 的每个子符的 index 进行遍历的,这样才可以成功访问完整个字符串
			if s[j] in st:
				# 这表示这个字符已经出现过了，就用一个i来记住上一次出现的位置
				i = max(st[s[j]],i)
				print(s[j],i)
			ans = max(ans,j-i+1) # 字符上一次出现的位置和当前出现的位置的差的最大值就是要求的最长子串
			st[s[j]] = j+1   # 每次当有一个字符访问过之后，st里面就存放该字符到前面的字符的长度
		return ans

# 测试
solution = Solution()
s = 'pwwkew'
print(solution.lengthOfLongestSubstring(s))
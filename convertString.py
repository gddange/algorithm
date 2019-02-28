#coding:utf-8

'''
给定一个字符串，以及指定的行数，需要将这个字符串按照指定的行数进行Z字形排列，排列顺序是从上往下，从左往右，然后再根据排列读取数组产生一个新的字符串
 h
比如：
input:'LEETCODEISHIRING',nrows=3
则排列为:
L   C   I   R
E T O E S I I G
E   D   H   N
output: LCIRETOESIIGEDHN
如果输入'LEETCODEISHIRING',nrows=4
则排列为:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
output:LDREOEIIECIHNTSG

这个就是说，每次从上往下排列之后，再去排列对角线上的字符
'''
class Solution:
	'''这种算法，时间复杂度是 O(n),只有一次循环而已，空间复杂度也是O(n)，因为最大就是每行都是n，存nrows ,多存了几个占位符'''
	def convert(self,s,nrows):
		news = []
		m=1
		last_index = 0
		while(last_index <len(s)):
			list1 = ['/n'] * nrows
			if m == 1:
				list1[:len(s[last_index:last_index + nrows])] = s[last_index:last_index + nrows]
				news.append(list1)
				last_index +=nrows
				m = nrows -1
				m = max(1,m)   # 这一步是为了保证 m 的最小值是 1,否则值超过下限就会出错
				continue
			m -=1
			list1[m] = s[last_index]
			last_index +=1
			news.append(list1)
		print(news)
		returns = ''
		news = zip(*news)
		print(news)
		for seq in news:
			for w in seq:
				if w != '/n':
					returns +=w
		return returns

	'''
	第二种解法，这种呢，是根据数学来的，只要知道每个字符应该在哪行即可
	首先，我们知道，每行中间的空白字符的个数，是nrows- 2,这 所以在一个矩阵内，一共读取了 nrwos * 2 +nrows-2 个数据
	'''

solution = Solution()
s = 'PAYPALISHIRING'
print(solution.convert(s,3))



		

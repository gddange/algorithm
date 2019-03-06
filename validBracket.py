#coding:utf-8

'''
给定一个字符串，其中的值只包括三种括号，'{}[]()',除此之外再无他值，判断这个字符串是不是能够闭合。
这是一个栈来解决的问题

闭合包括：1.左括号必须以相同类型的右括号闭合
        2.左括号必须以正确的顺序闭合
比如说：
input:'()'
output:True

input:'(]'
output:False

'''
class Solution:
	def isValid(self,s):
		# 假设输入的是空白，那就返回有效值
		if s.strip() == '':
			return True
		bracket = {'}':'{',']':'[',')':'('}   # 指定各个左括号与其右括号的对应关系
		# 给一个栈，遇到左括号就进栈，遇到右括号就出栈，如果最后访问完毕，但是栈里还有剩余就是 false
		stack = []
		for item in s:
			if item in bracket.values():
				stack.append(item)
			else:
				# 如果不在 values 那就是右括号
				# 如果出现右括号，但是左括号已经没有了，也是 False
				if len(stack) == 0:
					return False 
				if stack[-1] != bracket[item]:
					return False 
				else:
					del stack[-1]
		'''
		上面这段 for 循环还可以这样写，更加漂亮
		for char in s:
			if char in bracket:
				# 因为当他是右括号的时候要进行的操作更加多，所以对其做if操作更加好，这样的话，else 里就可以少写一点，整段代码看起来逻辑会更加清晰
				top_element = stack.pop() if stack else '#'  # 给一个定值给 top_element
				if top_element != bracket[char]:
					return False 
			else:
				stack.append(char)
		'''
		return not Stack  # 即栈为空的时候是正确的，这写法真的太漂亮了

solution = Solution()
s = ')['
print(solution.isValid(s))


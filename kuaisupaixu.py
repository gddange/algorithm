#coding:utf-8

alist = [6,2,7,3,8,9]

# 快速排序，每次选定一个值，然后用该值和 list 中其他值进行比较，首先先从 high 这个位置开始遍历，再移动 low指针
# 其基本思想就是，每次选定一个值，然后把比他大的放在一个组，右边，比他小的放在一个组，左边
def quickSort(l):
	if len(l) <2:
		return l 
	# 如果不是小于0 的时候，排序
	left,right = [],[]
	middle = l[0]
	l.remove(middle)
	for data in l:
		if data > middle:
			right.append(data)
		else:
			left.append(data)
	return quickSort(left) + [middle] + quickSort(right)

class Solution:
    def myAtoi(self, s) :
        s= s.lstrip()
        valid = list('0123456789') + ['-','+']
        if len(s) == 0 or s[0] not in valid:
            return 0
        x = ''
        if s[0] == '-':
            x +='-'
            s = s[1:]
        elif s[0] == '+':
        	x +='+'
        	s = s[1:]
        for word in s:
            if word in valid[:-2]:
               x +=word
            else:
                break
        if x == '-' or x == '+':
        	return 0
        x = int(x)
        if x > (2**31 - 1):
            x = 2**31 -1
        elif x < -2**31:
            x = -2**31
        return x
solution = Solution()
s = '3.14159'
print(solution.myAtoi(s))
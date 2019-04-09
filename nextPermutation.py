#coding:utf-8
'''
题目要求，实现获取下一个排列的函数，算法需要将给定的数字序列重新排列成为字典序列中下一个更大的序列
要求原地修改，只允许使用额外常数空间

例子：
input: 1,2,3 -> 1,3,2
input:3,2,1 -> 1,2,3
input: 1,1,5 -> 1,5,1
input: 1,3,2 - > 2,1,3
'''
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)-1,0,-1):
        	if nums[i] > nums[i-1]:
        		# 如果 i-1 < i 说明 i-1 和 i 下标的元素是升序排列的，这个时候只要处理 [i-1:] 的数据就能得到下一个大的排列了
        		temp = nums[i-1]
        		for j in range(len(nums)-1,i-1,-1):
        			if nums[j] > nums[i-1]:
        				nums[i-1] = nums[j]
        				nums[j] = temp
        				break
        		# 交换之后还要保证后续i-1后面的序列是升序的，只有这样得到的序列才是下一个大排序
        		low,high = i,len(nums)-1
        		while(low<high):
        			nums[low],nums[high] = nums[high],nums[low]
        			low +=1
        			high -=1
        		flag = True
        		break
        if not flag:
        	print('到降序这里了么')
        	i,j = 0,len(nums)-1
        	while(i<j):
        		temp = nums[i]
        		nums[i] = nums[j]
        		nums[j] = temp
        		i +=1
        		j -=1

nums = [2,3,1]
s = Solution()
s.nextPermutation(nums)
print(nums)
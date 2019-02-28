# coding:utf-8
'''
给定两个大小为 m 和 n 的有序数组， nums1 和 nums2
找出这两个有序数组的中位数，要求算法的时间复杂度是 O(log(m+n))
假设是 nums1 和 nums2 不会同时为空

比如：
 num1 = [1,3]
 num = [2]
 则中位是 2

再比如：
nums1 = [1,2]
nums2 = [3,4]
则中位数是 (2+3) /2 = 2.5
'''
import math

class Solution:
	def findMeidianSortedArray(self,nums1,nums2):
		total = []
		flag = True
		len1 = len(nums1)
		len2 = len(nums2)
		index1 = (len1/2 -1 if len1%2 == 0 else len1/2)
		middel1 = ((nums1[index1] + nums1[index1+1]))/2 if len1 %2 == 0 else nums1[index1]
		index2 = (len2/2 - 1 if len2%2==0 else len2/2) - 1
		middel2 = ((nums2[index2] + nums2[index2+1]))/2 if len2 %2 == 0 else nums2[index2]
		while (True):
			if len1==0:
				total.extend(nums2[middel2+1:])
				break
			if len2 == 0:
				total.extend(nums1[middel1+1:])
				break
			if middel1 < middel2:
				total.extend(nums1[:index1+1])
				len1 = len(nums1[index1+1:])
				index1 = len1/2 -1  + index1 if len1%2 ==0 else len1/2 + index1
				middel1 = (nums1[index1] + nums1[index1+1])/2 if len1 %2 ==0 else nums1[index1]
			elif middel1 == middel2:
				
			else:
				total.extend(nums2[:index2 +1])
				len2 = len(nums2[index2+1:])
				index2 = len2/2 -1  + index2 if len2%2 ==0 else len2/2 + index2
				middel2 = (nums2[index2] + nums2[index2+1])/2 if len2 %2 ==0 else nums2[index2]
		print(total)
		return (total[len(total) /2 -1] + total[len(total)/2 ])/2 if len(total) % 2==0 else total[len(total)/2]
solution = Solution()
nums1 = [1,3]
nums2=[2]
results = solution.findMeidianSortedArray(nums1,nums2)
print(results)




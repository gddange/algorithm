#coding:utf-8
'''
描述：给定两个有序数组，输出这两个有序数的中位数，要求算法的时间复杂度是O(log(m+n))

可以假设 nums1 和 nums2 不同是为空

比如：
nums1 = [1,3],nums2 = [2]
则输出：2.0

nums1 = [1,2],nums2 = [3,4]
则输出： 2+3/2 = 2.5

解题思路：
首先，这两个数组是有序的。所以在算法的实现过程中，这一点肯定是要利用的
然后关于这个算法的时间复杂度的要求，是 o(lon(m+n))说明，在循环的时候，应该是用了快速排序那样的划分方式

具体：
分为两步：
1.将 nums1 划分为两个部分，一共有m+1个划分方式（因为划分位置可以是[0,m]),同样的道理将 nums2 也划分为这样的两个部分
2.将两个划分的左边放到集合，left_part,右边放到 right_part.
   这样一来，只要满足两个条件，就能找到中位数：
    1): len(left_part) == len(right_part)
    2) max(left_part) == min(right_part)

假设在划分的时候，nums1共有 m 个数据，左边有 i 个数据，右边就有 m-i 个数据，而左边的最大值是 A[i-1],右边的最小值是 A[i]
假设 nums2（B）有 n 个数据，划分之后，左边有 j 个数据，右边有 n-j 个数据，左边的最大值是 B[j-1],右边的最小值是 B[j]

因此，在比较的时候，只要满足：
A[i-1] < B[j] and B[j-1] < A[i]  即是满足了上面的第二个条件

而一旦，在 A 里划分为： i 的时候，B就只需要 j = (m+n+1)/2 - i个数据添加到左边，即能满足 len(left_part) == len(right_part)

这里要考虑的是， (m+n+1)/2 -i >0 ,所以 n > m

因此发现，在循环的时候，只要 for m 个数据，然后划分 A ,接着在 B 里寻找填充的 index 即可，在循环的过程中，为了加快速度，按照如下的步骤来进行二叉树搜索：
  1） 设 imin = 0, imax = m,然后在 [imin,imax] 里搜索
  2） 令 i = (imin+imax)/2 ,j = (m+n+1)/2 - i
  3) 现在满足了 len(left_part) == len(right_part),但是会遇到如下三种情况：
     a. B[j-1] <= A[i] and A[i-1] <= B[j]，满足条件，循环停止
     b. B[j-1] > A[i]，这意味着 A[i] 太小，因此，需要调整 i 来使得 B[j-1] <= A[i].
        这时候，只能增加 i ，因为增加 i,那么才会满足 A[i] 在增加，同时 B[j-1]就要减小，因为当增加了 i，left part 里 B的部分就会变少。这个时候，搜索范围变为[i+1,imax]
     c. A[i-1] > B[j],这说明A中的数据太大了,因此需要减小A[i-1]，所以就要减小 i，搜索范围变为[imin,i-1]

考虑临界值：
在每次循环的是涉及到A[i],A[i-1],B[j],B[j-1]这四个数据。而index (i,i-1,j,j-1)有可能会出现，i=0,j=0,i=,j=n.这个时候，A[i-1],B[j-1],A[i],B[j]将会不存在，因此需要考虑这个特殊时候的处理

如果这四个值部分不存在，比如说 i=0 的时候，那么 A[j-1]不存在，即是说，就不需要判断 A[i-1] <= B[j]
不过这里要注意，j > 0 是恒成立的，因为 m < n ,所以 j = (m+n + 1)/2 - i 是满足恒大于0的
而一旦 i > 0,则满足 j = (m+n + 1) / 2 - i < (m+n+1)/2 - i < (m+n+1)/2 <= (n+n+1)/2 <=

所以只要考虑 i = 0时， j = n ?这两个临界值即可

'''

class Solutoin:
	def findMedianSortedArrays(self,nums1,nums2):
		'''首先是排序的时候 for 的是短的那个'''
		if len(nums1) > len(nums2):
			nums1,nums2 = nums2,num1 
		m,n = len(nums1),len(nums2)
		if n == 0:
			# 如果最大的那个数组长度都为0，那就不满足假设的两个数组不同时为空的
			raise ValueError
		imin,imax,i,j = 0,m,0,0
		while(imin <= imax):
			i = (imin + imax)/2
			j = (m + n + 1)/2 - i 
			if i < m and B[j-1] > A[i]:
				# 这个时候就是 i 太小
				imin = i + 1
			elif i > - and A[i-1] > B[j]:
				imax = i-1
			else:
				# 这个时候，就是两者条件都满足
				if i == 0: max_of_left = B[j-1]   # 要这样考虑 j == 0 ,以及 i== 0是因为，当 ==0 的时候，i-1,j-1 不存在，会出错
				elif j == 0:
					max_of_left = A[i-1]
				else:
					max_of_left = max(A[i-1],B[j-1])

				if (m + N) % 2 == 1:
					# 这个时候说明是奇数，因为左边的数据 == (m+n+1)/2 所以，左边的而数据要多一个，这一个就是middle
					return max_of_left
				if i == m:
					min_of_left = B[j]
				elif j == n:
					min_of_left = A[i]
				else:
					min_of_right = min(A[i],B[j])
				return (max_of_left + min_of_right) / 2.0


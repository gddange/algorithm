#coding:utf-8
'''
要求，输入一个list,以及一个整数 k,则每 k 个节点进行一次list 的反。k的值小于或者等于链表的长度，如果节点总数不是 k 的整数倍，那么
将剩余的节点保持原有的顺序

例：
input 1->2->3->4->5
if k == 2:
output: 2->1->4->3->5

if k== 3:
output: 3->2->1->4->5

要求:
算法只能使用常数的额外空间
不能只是单纯的改变节点的内部的值，而是要进行节点交换

思路，给一个 q,p，用来指示每次要更改之间的顺序，然后有一个 imap 用于存储待反转的 k 个 list 的指针
然后，每次访问，当 list　未访问完毕，同时遍历了 k 个待访问的值，那么进行一次反转，反转的时候利用 imap 里记录的待反转的指针来访问，避免重复遍历
'''

class ListNode:
	def __init__(self,val,next = None):
		self.val = val
		self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        num = 0
        p = head
        while(p != None):
            num +=1
            p = p.next
        if num < k:
            return head
        q = head
        p = head
        c,count,imap =0, 0,[]
        while(p!=None):
            imap.insert(0,p)
            count +=1
            p = p.next
            if count < k and p == None:
            	return head
            if(count == k):
                # 反转
                count = 0
                c +=1
                for i in range(len(imap) - 1):
                	# 反转，本身插入到 list 里就是倒序的，所以直接在 list 里顺序做操作即可
                    imap[i].next = imap[i+1]
                q.next = imap[0]   # 上一轮的 q 是指向上一轮反转过后的尾部的，因此在当前为了防止当前这部分链表丢失，要让上一轮尾部的那个 node 指向当前反转过后的头部节点
                q = imap[-1]       # 让 q 指向当前反转过后的尾部的 node
                if c == 1:
                	head = imap[0]   # 第一轮反转的时候，imap[0]就是整个后续的list的头
                q.next = p        # 让当前反转过后的尾部的 next 指向下一轮要反转的的头，这样，如果不进行反转操作也可以返回一整条的listnode
                imap = []  # 第一轮转完以后就要将imap给予空好继续下一轮
        return head

def createList(l):
	head = ListNode(l[0])
	p = head
	for item in l[1:]:
		p.next = ListNode(item)
		p = p.next
	return head

def print_list(l):
	while(l != None):
		print(l.val)
		l = l.next

temp = [1,2,3,4,5]
l = createList(temp)
solution = Solution()
ans = solution.reverseKGroup(l,k=1)
print_list(ans)
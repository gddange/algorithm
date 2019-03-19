#coding:utf-8
'''
关于二叉树的算法
'''

############################################################################
# 首先是二叉树的构造，二叉树的访问，前序，中序，后续
############################################################################

class TreeNode:
	# 树节点
	def __init__(self,val=None,left = None,right = None):
		# python 里面传递就是地址
		self.val = val
		self.left = left
		self.right = right


########################################################################
## 给定一个数组，根据数组中的数据来构建树
########################################################################
def createTree(root,l):
	# 按照前序遍历的算法进行构造，这样构造的二叉树可以是任意形状的
	if len(l) < 1:
		root = None
		return root
	c = l.pop(0)
	if c == None:
		root = None
	else:
		root = TreeNode(c)
		root.left = createTree(root,l)
		root.right = createTree(root,l)
	return root

##########################################################################
###                      树类                                          ###
##########################################################################

class Tree:
	'''树类'''
	def __init__(self,root,myqueue):
		self.root = root
		self.myqueue = myqueue    #　这个是待插入孩子的队列

	def add_node(self,elem):
		# 给树增加节点的操作，这样增加的节点必须是完全二叉树
		if self.root == None:
			self.root = TreeNode(elem)
			self.myqueue.append(root)
		else:
			cur = self.myqueue[0]
			if cur.left != None:
				cur.left = TreeNode(elem)
				myqueue.append(cur.left)
			else:
				cur.right = TreeNode(elem)
				myqueue.pop(0)    # 当一个父亲的左孩子右孩子都已经放完了数据，那么这个节点就可以从待插入孩子的队列当中删除了
				myqueue.append(cur.right)

	'''递归方式实现树的前序，中序，后续遍历'''
	def front_traversing(self,root):
		if root == None:
			return
		print(root.val)
		self.front_traversing(self,root.left)
		self.front_traversing(self,root.right)

	def middle_traversing(self,root):
		if root == None:
			return
		self.middle_traversing(root.left)
		print(root.val)
		self.middle_traversing(root.right)

	def last_traversing(self,root):
		if root == None:
			return
		self.last_traversing(self,root.left)
		self.last_traversing(self,root.right)
		print(root.val)

	'''利用堆栈实现树的前序中序后序遍历'''

	# 前序遍历，没访问完一个根节点，就将该根节点的值放入到 ans 当中，并且把该根节点放到 stack 里，如果左子树的跟节点全部访问完毕，那之后就是访问右子树，令根节点为右子树即可，当左右子树均访问完毕，则要将节点从 stack 里弹出
	def front_stack(self,root):
		stack,ans = [],[]
		while stack or root:
			while root:
				ans.append(root.val)
				stack.append(root)
				root = root.left()
			root = stack.pop().right
		return ans 

	# 中序遍历
	def middle_stack(self,root):
		stack,ans = [],[]
		while stack or root:
			while root:
				stack.append(root)
				root = root.left
			cur = stack.pop()  # 已经找到最左边的左节点，输出其值
			ans.append(cur.val)
			root = cur.right
		return ans

	# 后续遍历
	def back_stack(self,root):
		# tag 标签用来识别该节点右子树是否访问过了，不用 tag 的话，没有办法识别右子树是否访问
		stack,tag,ans = [],[],[]
		while stack or root:
			while root:
				tag.append(0)   # 访问了左子树，则 tag 为 0
				stack.append(root)
				root = root.left
			if tag[-1] == 1:
				# 1是访问过右子树，那么输出该节点并将其从 stack 里弹出即可
				tag.pop()
				cur = stack.pop()
				ans.append(cur.val)
			else:
				# 如果没有访问过右子树，那么就继续去访问右子树
				tag[-1] = 1
				root = stack[-1].right
		return ans

###############################################################################
#######                       test                                     ########
###############################################################################

l = ['A','B','C',None,None,'D',None,None,'E',None,None]
#l = [1,None,2,3]
root = None
print('start 构造树...')
ans = createTree(root,l)
print('end 构造树...')
print('前序结果：',front_stack(ans))
print('中序结果:',inorderTraversal(ans))
print('后序结果:',back_stack(ans))
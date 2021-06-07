# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#recursive
res = [] #store traversal result
def pre_order(root):
    if not root: return
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)

#iterative method 1 DFS
stack = [root]
res = [] #store traversal result
while stack:
    root = stack.pop()
    res.append(root.val)
    if root.right: stack.append(root.right)
    if root.left: stack.append(root.left)

#iterative method 2
stack = []
res = []
while root or stack:
    # 从根节点开始，一直找它的左子树
    while root:
        res.append(root.val)
        stack.append(root.val)
        root = root.left
    # while结束表示当前节点node为空，即前一个节点没有左子树了
    root = stack.pop()
    # 开始查看它的右子树
    root = root.right

#iterative method 3
stack = []
res = []
while root or stack:
    if root:
        stack.append(root) #先访问根节点
        res.append(root.val)
        root = root.left
    else:
        root = stack.pop() #回溯至父节点
        root = root.right

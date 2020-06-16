# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#recursive
res = [] #store traversal result
def in_order(root):
    if not root: return
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)

#iterative method 1
stack = []
res = [] #store traversal result
while root or stack:
    # 从根节点开始，一直找它的左子树
    while root:
        stack.append(root)
        root = root.left
    # while结束表示当前节点node为空，即前一个节点没有左子树了
    root = stack.pop()
    res.append(root.val)
    # 开始查看它的右子树
    root = root.right

#iterative method 2
stack = []
res = [] #store traversal result
while root or stack:
    if root:
        stack.append(root)
        root = root.left
    else:
        root = stack.pop()
        res.append(root.val)
        root = root.right



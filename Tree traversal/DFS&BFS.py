# root: binary tree root ndoe
# root.left, root.right, root.val
root = TreeNode

#DFS using stack
stack = [root]
while stack:
    node = stack.pop() # first in - last out
    #operation...
    #先右后左
    if node.right: stack.append(node.right)
    if node.left: stack.append(node.left)



#BFS using queue
queue = [root()]
while queue:
    node = queue.pop(0) # first in - first out
    #operation ....
    #先左后右
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)


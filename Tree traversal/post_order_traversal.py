#根节点
root = Treenode

#递归
res = []
def post_order(root):
    if not root: return
    post_order(root.left)
    post_order(root.right)
    res.append(node.val)

#iterative

#第一种迭代方法
#改编自前序遍历的递归解法，因为前序遍历是 node->node.left->node.right
# 我们需要想改变遍历顺序 node->node.right->node.left
# 在对结果进行reverse，就变成了 node.left->node.right->node 即为后序遍历
stack = [root]
while stack:
    node = stack.pop()
    if node.right: stack.append(node.right)
    if node.left: stack.append(node.left)
    res.append(node.val)
res.reverse()
return res



#第二种迭代方法
#颜色标记法
# 因此，我在这里介绍一种“颜色标记法”（瞎起的名字……），兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码。

# 其核心思想如下：

# 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
# 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
# 如果遇到的节点为灰色，则将节点的值输出

#######################################################
# 栈是一种 先进后出的结构，中序遍历出栈顺序为左，中，右
# 那么入栈顺序必须调整为倒序，也就是右，中，左

# 同理，如果是前序遍历，入栈顺序为 右，左，中；后序遍历，入栈顺序中，右，左

white, red = 0, 1
res = []
stack = [(white, root)]
while stack:
    color, node = stack.pop()
    if not node: continue
    if color == white:
        stack.append((red, node))
        stack.append((white, node.right))
        stack.append((white, node.left))
    else:
        res.append(node.val)
return res

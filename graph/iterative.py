from TreeNode import BinaryTreeNode, withVisitedNode
from collections import deque

def dfsPreOrderIterative(root: BinaryTreeNode):
    """
        Use a STACK
         
        current Node -> left child -> right child
    """
    print("Iterative - Pre Order Traversal")

    stack = [root]
    res = []
    while stack:
        node = stack.pop() 
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def dfsInOrderIterative(root: BinaryTreeNode):
    """
        Use a STACK

        left child -> current value -> right child
    """
    print("Iterative - In Order Traversal")

    stack = [withVisitedNode(root)]
    res = []
    while stack:
        node = stack.pop()

        if node.visited:
            res.append(node().val)
            continue

        # append in reverse order to get the rigth traversal: right -> current -> left (top of stack)
        if node().right:
            stack.append(withVisitedNode(node().right))

        node.visited = True
        stack.append(node)

        if node().left:
            stack.append(withVisitedNode(node().left))
    return res


def dfsPostOrderIterative(root: BinaryTreeNode):
    """
        Use a STACK

        left node -> right node -> current node
    """
    print("Iterative - Post Order Traversal")

    stack = [withVisitedNode(root)]
    res = []
    while stack:
        node = stack.pop()

        if node.visited:
            res.append(node().val)
            continue

        # append in reverse order to get the rigth traversal: current -> right -> left (top of stack)
        node.visited = True
        stack.append(node)

        if node().right:
            stack.append(withVisitedNode(node().right))
        
        if node().left:
            stack.append(withVisitedNode(node().left))
        
    return res

def BFS(root: BinaryTreeNode):
    """
        Use a QUEUE

        first level nodes -> second level -> .. leaf nodes
    """
    print("BFS")

    queue = deque([root])
    res = []
    # take all children of the current node and put them at the *end* of the queue. then process the next element
    while queue:
        node = queue.popleft()

        res.append(node.val)
        
        # since its a queue, we keep the same order as traversal
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
        
    return res


def dfsInOrderRecursive(root: BinaryTreeNode):
    """
        Recursively call dfs, first on the left, then add the node's value
          then recurse on the right child
    """
    print("Recursive - In Order Traversal")
    def dfs(root, res):
        if root is None:
            return
            
        if root.left:
            dfs(root.left, res)

        res.append(root.val)

        if root.right:
            dfs(root.right, res)

    res = []
    dfs(root, res)
    return res

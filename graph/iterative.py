from TreeNode import TreeNode, withVisitedNode,  generateBST

def dfsPreOrderIterative(root: TreeNode):
    """
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


def dfsInOrderIterative(root: TreeNode):
    """
    """
    print("Iterative - In Order Traversal")

    stack = [withVisitedNode(root)]
    res = []
    while stack:
        node = stack.pop()

        if node.visited:
            res.append(node().val)
            continue

        if node().right:
            stack.append(withVisitedNode(node().right))

        node.visited = True
        stack.append(node)

        if node().left:
            stack.append(withVisitedNode(node().left))
    return res


def dfsPostOrderIterative(root: TreeNode):
    """
    """
    print("Iterative - Post Order Traversal")

    stack = [withVisitedNode(root)]
    res = []
    while stack:
        node = stack.pop()

        if node.visited:
            res.append(node().val)
            continue

        node.visited = True
        stack.append(node)

        if node().right:
            stack.append(withVisitedNode(node().right))
        
        if node().left:
            stack.append(withVisitedNode(node().left))
        
    return res

def dfsInOrderRecursive(root: TreeNode):
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


if __name__ == "__main__":
    root = generateBST()
    print(dfsInOrderRecursive(root))
    print(dfsInOrderIterative(root))
    print(dfsPreOrderIterative(root))
    print(dfsPostOrderIterative(root))
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  

class NodeAttribute:    
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)        
    
    def __set__(self, obj, value):
        if not isinstance(value, TreeNode):
            raise ValueError(f"Wrong Value Type {value} for {self.public_name}")
        setattr(obj, self.private_name, value)

class withVisitedNode:
    n = NodeAttribute()

    def __init__(self, node):
        self.n = node
        self.visited = False

    def __call__(self):
        return self.n

def generateBST() -> TreeNode:
    """ Binary Search Tree
              4
           /     \
          2        6
         /  \     / \
        1    3   5   7
    """
    return TreeNode(4,
        TreeNode(2, 
                TreeNode(1), TreeNode(3) ),
        TreeNode(6, 
                TreeNode(5), TreeNode(7) )
    )        
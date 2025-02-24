class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children  


class BinaryTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None):
        children = [None, None]

        if left is not None:
            children[0] = left
        if right is not None:
            children[1] = right

        super().__init__(val, children)

    @property
    def left(self):
        return self.children[0]
    
    @property
    def right(self):
        return self.children[1]


class NodeType:
    """ Descriptor Protocol to check for TreeNode Type (https://docs.python.org/3/howto/descriptor.html)
    """
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)        
    
    def __set__(self, obj, value):
        if not isinstance(value, BinaryTreeNode):
            raise ValueError(f"Wrong Value Type {value} for {self.public_name}")
        setattr(obj, self.private_name, value)

class withVisitedNode:
    n = NodeType()

    def __init__(self, node):
        self.n = node
        self.visited = False

    def __call__(self):
        return self.n
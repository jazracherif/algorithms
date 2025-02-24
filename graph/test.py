import pytest
from TreeNode import BinaryTreeNode
from iterative import  \
    dfsInOrderRecursive, \
    dfsInOrderIterative, \
    dfsPreOrderIterative, \
    dfsPostOrderIterative, \
    BFS

@pytest.fixture()
def data() -> BinaryTreeNode:
    """ Binary Tree
              4
           /     \
          2        6
         /  \     / \
        1    3   5   7
    """
    return BinaryTreeNode(4,
        BinaryTreeNode(2, 
                BinaryTreeNode(1), BinaryTreeNode(3) ),
        BinaryTreeNode(6, 
                BinaryTreeNode(5), BinaryTreeNode(7) )
    )        


def test_dfsInOrderRecursive(data):
    assert dfsInOrderRecursive(data) == [1, 2, 3, 4, 5, 6, 7]

def test_dfsInOrderIterative(data):
    assert dfsInOrderIterative(data) == [1, 2, 3, 4, 5, 6, 7]

def test_dfsPreOrderIterative(data):
    assert dfsPreOrderIterative(data) == [4, 2, 1, 3, 6, 5, 7]

def test_dfsPostOrderIterative(data):
    assert dfsPostOrderIterative(data) == [1, 3, 2, 5, 7, 6, 4]

def test_BFS(data):
    assert BFS(data) == [4, 2, 6, 1, 3, 5, 7]

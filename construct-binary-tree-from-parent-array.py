"""
Given an array parent that is used to represent a tree. The array indices (0-based indexing) are the values of the tree nodes and parent[i] denotes the parent node of a particular node. The parent of the root node would always be -1, as there is no parent for the root. Construct the standard linked representation of Binary Tree from this array representation and return the root node of the constructed tree.

Note: If two elements have the same parent, the one that appears first in the array will be the left child and the other is the right child. You don't need to print anything, the driver code will print the level order traversal of the returned root node to verify the output.

Examples:

Input: parent[] = [-1, 0, 0, 1, 1, 3,5]
Output: 0 1 2 3 4 5 6
"""

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        data = {}
        for i, p in enumerate(parent):
            if p == -1:
                data[i] = Node(i)
                root = data[i]
            else:
                data[i] = Node(i)
        
        for i, p in enumerate(parent):
            if p != -1:
                if data[p].left is None:
                    data[p].left = data[i]
                else:
                    data[p].right = data[i]
        
        return root

        
        
    
if __name__ == "__main__":
    sol = Solution()
    parent = [-1, 0, 0, 1, 1, 3,5]
    print(f"The root of the Binary Tree is : {sol.createTree(parent=parent)}")
    # for i, p in enumerate(parent):
    #     print(i, "\t", p)
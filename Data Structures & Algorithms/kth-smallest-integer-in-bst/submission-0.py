# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.array = []
        self.traverse(root)
        print(self.array)
        return self.array[k-1]

    def traverse(self, root):
        if root is None:
            return
        
        self.traverse(root.left)
        # print(root.val)
        self.array.append(root.val)
        self.traverse(root.right)

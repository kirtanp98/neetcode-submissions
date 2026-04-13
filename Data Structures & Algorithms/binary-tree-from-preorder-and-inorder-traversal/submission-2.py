# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map = {v: i for i,v in enumerate(inorder)}
        self.rootp = 0
        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[self.rootp])
            pivot = map[preorder[self.rootp]]

            self.rootp +=1

            root.left = helper(left, pivot-1)
            root.right = helper(pivot+1, right)
            return root
        return helper(0, len(inorder) - 1)
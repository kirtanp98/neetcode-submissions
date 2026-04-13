# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0

        def helper(root, maxValue):
            if root is None:
                return
            
            if root.val >= maxValue:
                print('we got something', root.val)
                self.total += 1
                maxValue = root.val
                print(maxValue)
            
            lnum = helper(root.left, maxValue)
            rnum = helper(root.right, maxValue)

        helper(root, root.val)

        return self.total 
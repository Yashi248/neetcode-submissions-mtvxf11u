# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(curr,max_val):
            if curr.val >= max_val:
                self.count +=1
                max_val = curr.val
            
            if curr.left:
                dfs(curr.left,max_val)
            if curr.right:
                dfs(curr.right,max_val)
            
        dfs(root,root.val)
        return self.count
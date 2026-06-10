# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        if not root:
            return []
        
        d = deque([root])
        while d:
            level_list = []
            for i in range(len(d)):
                node = d.popleft()
                level_list.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            final.append(level_list)
        
        return final

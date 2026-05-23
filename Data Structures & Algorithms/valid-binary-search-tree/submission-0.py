# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False
        
        stack = []
        stack.append([root, -float("inf"), float("inf")])

        while stack:
            cur = stack.pop()
            if not cur[1] < cur[0].val < cur[2]:
                return False
            
            if cur[0].left:
                stack.append([cur[0].left, cur[1], cur[0].val])
            
            if cur[0].right:
                stack.append([cur[0].right, cur[0].val, cur[2]])
        
        return True


        
# Source : https://leetcode.com/problems/count-complete-tree-nodes
# Author : zheyuuu
# Date   : 2020-08-07

##################################################################################################### 
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all 
# nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive 
# at the last level h.
# 
# Example:
# 
# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# 
# Output: 6
#####################################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def getDepth(node, d):
            if not node:
                return 0
            if d==0:
                return getDepth(node.left, d)+1
            else:
                return getDepth(node.right, d)+1
        def canFind(node, path):
            while(path):
                d = path.pop()
                if d==0:
                    node = node.left
                else:
                    node = node.right
                if not node:
                    return False
            return True
            
        n = getDepth(root, 0)
        m = getDepth(root, 1)
        print(m,n)
        if m==n:
            return 2**n-1
        l,r = 2**(n-1), 2**n-1
        while(l<r):
            mid = (l+r)//2
            path = []
            t = mid
            while(t!=1):
                path.append(t&1)
                t = t>>1
            if canFind(root, path):
                l = mid+1
            else:
                r = mid
        return l-1
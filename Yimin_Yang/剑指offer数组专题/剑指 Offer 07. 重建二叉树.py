# 剑指 Offer 07. 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 示例 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 示例 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Author: Yimin Yang
# Date: Nov 20, 1998


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # If the preorder is not existance, then return None.
        if inorder:
            # find the root in the inorder
            ind = inorder.index(preorder.pop(0))
            # get the loc of root
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0: ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

        # # Recursive algorithm
        # def dfs(root, left, right):
        #     if left > right: return
        #     node = TreeNode(preorder[root])
        #     i = dic[preorder[root]]
        #     node.left = recur(root + 1, left, i - 1) 
        #     node.right = recur(i - left + root + 1, i + 1, right)
        #     return node

        # dic = {}
        # preorder = preorder
        # for i in range(len(inorder)):
        #     dic[inorder[i]] = i
        # return dfs(0, 0, len(inorder) - 1)

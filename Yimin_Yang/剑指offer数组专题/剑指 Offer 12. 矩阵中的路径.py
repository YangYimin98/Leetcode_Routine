# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

# 示例 1：

# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：

# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Author： Yimin Yang
# Date: Nov 21, 2021

# 算法思路：dfs（深度优先搜索）-----> 破坏现场，恢复现场：到达过的值取空，dfs之后再恢复成原先的值
# dfs function：选择跳出标志，本题有三点：（1）索引不在board边界---->false;（2）当前的对应字母在word中压根不存在---->false；（3）k的长度和word长度一致，说明匹配成功


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i <= len(board) - 1: return False
            if not 0 <= j <= len(board[0]) - 1: return False
            if board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            temp = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            board[i][j] = word[k]
            return temp
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True 
        return False

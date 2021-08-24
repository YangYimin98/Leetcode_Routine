# 给定一个 m二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）

# 来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 x n 



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

      def dfs(i, j, k):  # i和j是当前元素在矩阵中的行列索引，k是字符的索引
        if not 0 <= i <len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:#是否越界和第一个字母是否匹配
          return False
        if k == len(board) - 1:
          return True 
        board[i][j] = ''
        res = dfs[i+1, j, k+1] or dfs(i-1,j,k=1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
        board[i][j] = word[k]
        return res
      for i in range(len(board)):
        for j in range(len(board)-1):
          if dfs(j, j, 0):
            return True
      return False

# 给定一个 m二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）

# 来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 x n 


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
                return False
            if board[i][j] != word[k]:  #当前字符，所以必须在第一个if判断下面，否则会溢出
                return False
            if k == len(word) - 1:
                return True
            
            board[i][j] = ''  #查询过的就设置为空字符串，防止反复查询
            temp = dfs(i-1,j, k+1) or dfs(i+1, j, k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            board[i][j] = word[k] # 还原现场
            return temp
        for i in range(len(board)):# 开始遍历
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False



            

# 题目：在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 示例： [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。

# 算法思路:
# 从矩阵 matrix 左下角元素（索引设为 (i, j) ）开始遍历，并与目标值对比：
# 当 matrix[i][j] > target 时，执行 i-- ，即消去第 i 行元素；
# 当 matrix[i][j] < target 时，执行 j++ ，即消去第 j 列元素；
# 当 matrix[i][j] = target 时，返回 true ，代表找到目标值。
# 若行索引或列索引越界，则代表矩阵中无目标值，返回 false 。

# 作者：Yimin Yang
# 日期：Nov 19, 2021
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        # Method: Considering a binary search tree
        j, i = 0, len(matrix) - 1
        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            elif matrix[i][j] == target: return True 
        return False


        # # Rubbish Method
        # for i in range(len(matrix) - 1):
        #     for j in range(len(matrix[0]) - 1):
        #         if target == matrix[i][j]:
        #             return True
        # return False

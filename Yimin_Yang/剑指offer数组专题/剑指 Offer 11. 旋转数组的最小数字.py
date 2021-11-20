# 剑指 Offer 11. 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

# 示例 1：

# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：

# 输入：[2,2,2,0,1]
# 输出：0

# Author: Yimin Yang
# Date: Nov 20 2021

# 算法思路：
#（1）暴力枚举： 遍历数组并排序，取第一个即可
# （2）二分法： 首先取数组的俩边端值的索引i和j，遍历数组，取中间值的索引，如果middle对应的值比j大，证明所求值一定在middle右边，反之在数组# 左边，若相等，则往左边移动一格即可
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # # Method 1: Stupid method----> Directly Traverse
        # numbers.sort()
        # return numbers[0]

        # Method 2:dichotomy
        i, j = 0, len(numbers) - 1
        while i < j:
            pivot = (j - i) // 2 + i
            if numbers[j] > numbers[pivot]: j = pivot
            elif numbers[j] < numbers[pivot]: i = pivot + 1
            else: j -= 1
        return numbers[i]

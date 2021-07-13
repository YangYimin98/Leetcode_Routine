"""把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


"""算法思路：
找到数组中最大的数的索引
最大的数之后的序列全部切割放到原数组的前面
返回num[0]
"""


class Solution:
    '''not good choice'''
    def minArray_1(self, numbers):
        list_cut = []
        ind = numbers.index(max(numbers))
        if numbers[ind] == numbers[ind + 1]:
            ind += 1
        list_cut.append(numbers[ind + 1:])
        return list_cut[0][0]

    '''also not that good'''
    def minArray_2(self, numbers):
        return min(numbers)

    def minArray_3(self, numbers):
        """二分查找"""
        left, right = 0, len(numbers) - 1
        while left < right:
            pivot = left + (right - left) // 2
            if numbers[pivot] < numbers[right]:
                right = pivot
            elif numbers[pivot] > numbers[right]:
                left = pivot + 1
            else:
                right -= 1
        return numbers[left]



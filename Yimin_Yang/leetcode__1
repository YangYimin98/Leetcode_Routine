"""数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。
请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-majority-element-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:

    def solution(self, num):
        for i in set(num):
            if num.count(i) > len(num) / 2:
                return i
        return -1
        
        """use dictionay"""
        # nums = set(num)
        # frequency = {}
        # for i in nums:
        #     c = num.count(i)
        #     frequency[c] = i
        # a = max(frequency.keys())
        # if a > len(num) / 2:
        #     return frequency[a]
        # else:
        #     return -1


"""Instance"""
test = [3, 2, 1]
s = Solution()
print(s.solution(test))

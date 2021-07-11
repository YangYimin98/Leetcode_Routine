"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""

# """out of time"""
# from functools import lru_cache
#
#
# class Solution:
#     def numWays(self, n: int) -> int:
#         lru_cache()
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         else:
#             return (self.numWays(n - 2) + self.numWays(n - 1)) % 1000000007


class Solution:

    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        else:
            a, b, temp = 1, 1, 0
            for _ in range(2, n + 1):
                temp = (a + b) % 1000000007
                a = b
                b = temp
            return temp


# s = Solution()
# print(s.numWays(100))











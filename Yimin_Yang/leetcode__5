"""写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下："""


# """iteration approach"""
#
#
class Solution:

    def fib(self, n):

        if n < 2:
            return n
        else:
            a, b, temp = 0, 1, 0
            for _ in range(2, n + 1):
                temp = (a + b) % 1000000007
                a = b
                b = temp
            return temp


"""recursive approach"""

#
# class Solution:
#
#     def __init__(self):
#         self.dic = {0: 0, 1: 1}
#
#     def fib(self, n):
#         if n in self.dic:
#             return self.dic[n]
#
#         return (self.fib(n - 2) + self.fib(n - 1)) % 1000000007













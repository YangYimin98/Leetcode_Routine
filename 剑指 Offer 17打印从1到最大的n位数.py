"""输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999"""



class Solution:
    def printNumbers(self, n: int) -> List[int]:
        def dfs(ind, num, digit):
            if ind == digit: 
                temp.append(int(''.join(num))) 
                return
            for i in range(0, 10):
                num.append(str(i))
                dfs(ind + 1, num, digit)
                num.pop()
        temp = []
        for i in range(1, n +1):
            for j in range(1, 10):
                num = [str(j)]
                dfs(1, num, i)
        return temp



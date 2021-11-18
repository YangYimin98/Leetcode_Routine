# 找出数组中重复的数字。


# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Author: Yimin Yang
# Date: Nov 19. 2021

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        # # First build a hash table
        # hash = set()
        # # Then go through the array, if the target num is already in the hash, then return it, o
        # # Otherwise add it to the hash
        # for i in nums:
        #     if i in hash:
        #         return i
        #     else: hash.add(i)

        # # Method 2(Sightly worse time complexity performance, even worse space complexity performance instead)
        # # Use an array
        # list = []
        # for i in nums:
        #     if i in list:
        #         return i
        #     list.append(i)

        # Method 3(Copy: Self hash)
        # All the values of the list will between 0 and n-1
        # Then it means every index will have one or more targeted values.

        # Traverse the nums, if nums[i] == i, means the num has already found the correct index, continue
        # If nums[nums[i]] == nums[i], means found the repeat value
        # Otherwise put the value in the index position
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


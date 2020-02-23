"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    解法1：快速排序。做不出来，因为不能保证数量一致就是对的，例如，5之前如果是4个数就认为对，有可能是4个1
    解法2： 一个萝卜一个坑，假设长度为i，则从0到i遍历数组，跳过0或负数，看是否应该在对应的位置，若不在且原位置数也不对，则与该位置交换。最后从0开始找第一个不对的数
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        numsL = len(nums)
        if numsL == 0:
            return 1
        for i in range(0,numsL):
            cu = nums[i]
            if cu > numsL or cu < 1:
                continue
            if cu != i+1 and nums[cu -1] != cu:
                while True:
                    j = cu - 1
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    newCu = nums[i]
                    if newCu > numsL or newCu < 1:
                        break
                    cu = newCu
                    if cu == i + 1 or nums[cu - 1] == cu:
                        break

        for i in range(0,numsL):
            cu = nums[i]
            if cu != i+1:
                return i+1
        return numsL + 1
    def swap(self, nums: List[int], i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
s = Solution()
print(s.firstMissingPositive([1]))


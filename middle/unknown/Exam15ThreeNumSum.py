from typing import List

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
思路：
1、排序
2、遍历数组
双指针，一个从i+1向右，一个从n-1向左，找和是0的

"""
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    re = []
    if len(nums) < 3:
        return None
    min = (nums[len(nums) - 1] + nums[len(nums) - 2]) * -1
    max = (nums[0] + nums[1]) * -1
    maxIdex = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if (nums[i] <= max):
            maxIdex = i
            break
    for i in range(len(nums)):
        if nums[i] < min or nums[i] > 0 or (i > 0 and nums[i] == nums[i - 1]):
            continue
        begin = i + 1
        end = maxIdex
        while True:
            if nums[begin] + nums[end] + nums[i] == 0 and begin < end:
                sRe = []
                sRe.append(nums[i])
                sRe.append(nums[begin])
                sRe.append(nums[end])
                re.append(sRe)
            if nums[begin] + nums[end] + nums[i] < 0:
                while True:
                    begin += 1
                    if begin > end or nums[begin] != nums[begin-1]:
                        break
            elif nums[begin] + nums[end] +nums[i] > 0:
                while True:
                    end -=1
                    if end < begin or nums[end] != nums[end+1]:
                        break
            else:
                while True:
                    begin += 1
                    if begin > end or nums[begin] != nums[begin-1]:
                        break
                while True:
                    end -=1
                    if end < begin or nums[end] != nums[end+1]:
                        break
            if begin >= end :
                break
    return re
# nums = [-1, 0, 1, 2, -1, -4]
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

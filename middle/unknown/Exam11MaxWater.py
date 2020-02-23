"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


# 思路:两个指针从两端开始，较矮的那个分别向左或向右移动，移动到比前一个高
def maxArea(height: List[int]) -> int:
    max = 0
    begin = 0
    end = len(height) - 1
    while True:
        re = (end - begin) * min(height[begin], height[end])
        if re > max:
            max = re
        if height[begin] < height[end]:
            nextBegin= begin+1
            while nextBegin < end and height[nextBegin] < height[begin]:
                nextBegin = nextBegin + 1
            begin = nextBegin
        else:
            nextEnd = end -1
            while nextEnd > begin and height[nextEnd] < height[end]:
                nextEnd = nextEnd - 1
            end = nextEnd
        if begin >= end:
            break
    return max
testlist = [1,8,6,2,5,4,8,3,7]
print(maxArea(testlist))

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        for i in lists:
            q.put((i, i.val))
        head = q.get()[0]
        cu = head
        if cu.next is not None:
            q.put((cu.next, cu.val))
        while True:
            tmp = q.get()[0]
            if tmp is None:
                break
            cu.next = tmp
            q.put((tmp.next,tmp.val))
        return head


n1 = ListNode(5)
n2 = ListNode(6)
l = [n1, n2]
Solution().mergeKLists(l)

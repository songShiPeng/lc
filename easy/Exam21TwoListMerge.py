"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
思路：
1、先找到头结点改在哪
2、比较两个子列表的头结点哪个小
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cu1 = l1
        cu2 = l2
        if cu1.val < cu2.val:
            head = cu1
            cu1 = cu1.next
        else:
            head = cu2
            cu2 = cu2.next
        cu = head
        while cu1 is not None and cu2 is not None:
            if cu1.val < cu2.val:
                cu.next = cu1
                cu = cu1
                cu1 = cu1.next
            else:
                cu.next = cu2
                cu = cu2
                cu2 = cu2.next
        if cu1 is not None:
            cu.next = cu1
        elif cu2 is not None:
            cu.next = cu2
        return head




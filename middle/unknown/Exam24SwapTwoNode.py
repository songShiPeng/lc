"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        newHead = head.next
        if newHead is None:
            return head
        """
        交换前：
        cu表示前一个节点
        nextNode后一个节点
        pre表示指向cu的节点
        """
        cu = head
        nextNode = newHead
        pre = None
        while True:
            if cu is None:
                break
            cu.next = nextNode.next
            nextNode.next = cu
            if pre is not None:
                pre.next = nextNode
            pre = cu
            cu = cu.next
            if cu is None or cu.next is None:
                break
            nextNode = cu.next
        return newHead





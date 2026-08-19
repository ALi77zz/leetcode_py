'''
Author: Lipc
Date: 2026-08-19 18:14:43
LastEditTime: 2026-08-19 18:58:35
Description: leetcodeHot100第160题：相交链表
FilePath: \python\hot100\160相交链表.py
'''
from __future__ import annotations

# 解法一：暴力解法
# """
#     思路：
#     先确定两个链表的长度lenA和lenB，计算两条链表长度差len1
#     长的先走len1步，然后两个链表同时走，看有没有相交的
# """
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         if headA is None or headB is None:
#             return None
#         headA1 = headA 
#         headB1 = headB
#         # lenA 和 lenB 来计算两个链表的长度
#         lenA = 0
#         lenB = 0
#         while(headA1 != None):
#             lenA += 1
#             headA1 = headA1.next
#         while(headB1 != None):
#             lenB += 1
#             headB1 = headB1.next
#         # 计算两条链表长度差
#         len1 = lenA-lenB if lenA > lenB else lenB-lenA
#         # 长的先走
#         if lenA > lenB:
#             while(len1 > 0):
#                 len1 -= 1
#                 headA = headA.next
#         elif lenA < lenB:
#             while(len1 > 0):
#                 len1 -= 1
#                 headB = headB.next
#         # 同时走看有没有相交的
#         while(headA != None and headB != None):
#             if(headA == headB):
#                 return headA
#             headA = headA.next
#             headB = headB.next
#         return None

# 解法二：
"""
    思路：
    1.两个链表分别走完自己的路程
    2.接着走对方的路程
    这样两个链表的总路程是一样的，假设listA长度为a，listB长度为b，a+b = b+a
    3.如果两个链表相交，那么在走完a+b的路程后，两个指针会同时到达相交点，若走完a+b的路程后还没有相交，那么两个链表就不相交
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 创建两个节点用来遍历链表
        headA1 = headA
        headB1 = headB
        # 各自走a+b的路程
        # 循环结束时，headA1和headB1要么相交，要么都为None
        while(headA1 != headB1):
            # 如果走到链表尾部，就让它走另一条链表
            if headA1 != None:
                headA1 = headA1.next
            else:
                headA1 = headB

            if headB1 != None:
                headB1 = headB1.next
            else:
                headB1 = headA
        # 如果相交，返回相交点；如果不相交，返回None
        return headB1
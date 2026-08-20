'''
Author: Lipc
Date: 2026-08-20 23:25:56
LastEditTime: 2026-08-20 23:53:16
Description: 
FilePath: \python\hot100\206反转链表.py
'''

# 1->2->3->4->5
# pre->None current->1->2->3->4->5
# temp->current.next == 2
# pre->1->None
# pre->2->1->None
# pre->3->2->1->None
pre = None
current = head
while current:
    temp = current.next
    current.next = pre
    pre = current
    current = temp
# temp来保存current的下一个节点，防止丢失
# 将current的next指向pre
# pre移动到current
# current移动到temp
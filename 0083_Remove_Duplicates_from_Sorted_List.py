# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            ptr = head
            while ptr.next != None:
                if ptr.next.val != ptr.val:
                    ptr = ptr.next
                    continue
                else:
                    if ptr.next.next == None:
                        ptr.next = None
                        return head
                    else:
                        ptr.next = ptr.next.next
                        continue
            return head

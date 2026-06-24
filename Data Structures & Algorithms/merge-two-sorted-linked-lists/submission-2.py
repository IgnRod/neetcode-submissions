# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        iter = None
        if(not (list1 and list2)):
            return list1 if list1 else list2
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1=list1.next
        else:
            head = ListNode(list2.val)
            list2=list2.next
        iter = head
        chose = None
        while(list1 or list2):
            if(not list1):
                chose = list2.val
                list2=list2.next
            elif(not list2):
                chose = list1.val
                list1=list1.next
            elif(list1.val <= list2.val):
                chose = list1.val
                list1=list1.next
            elif(list1.val >= list2.val):
                chose = list2.val
                list2=list2.next
            iter.next = ListNode(chose)
            iter = iter.next
        return head

        


        
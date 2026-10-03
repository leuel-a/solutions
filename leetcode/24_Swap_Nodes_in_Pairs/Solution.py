# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        swapIndex = 0
        newHead = None
        prev, prevPrev, curr = None, None, head

        while curr:
            if swapIndex % 2 != 0:
                if prevPrev is not None:
                    prev.next = curr.next
                    curr.next = prev
                    prevPrev.next = curr

                    prevPrev = curr
                    curr = prev.next
                else:
                    prev.next = curr.next
                    curr.next = prev

                    newHead = curr
                    prevPrev = curr
                    curr = prev.next
            else:
                if prev is None:
                    prev = curr
                else:
                    prevPrev = prev
                    prev = curr
                curr = curr.next
            swapIndex += 1
        return newHead if newHead is not None else head


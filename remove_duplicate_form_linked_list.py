class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        first = head
        prev = None
        
        while first and first.next:
            temp = None
            if first.val == first.next.val:
                temp = first.next
                while temp.next and first.val == temp.next.val:
                    temp = temp.next
                
                if prev == None and temp.next == None:
                    head = None
                    break
                    
                if prev == None:
                    head = temp.next
                    
                else:
                    prev.next = temp.next
                
                first = temp.next
            
            else:
                prev = first
                first = first.next
        return head

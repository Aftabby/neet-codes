class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self, first_node_value):
        self.head = ListNode(first_node_value)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            curr.next = curr.next.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, ' -> ')
            curr = curr.next
        print()
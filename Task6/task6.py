""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def sorted_insert(head, data):
    if head is None or head.data > data:
        return push(head, data)
    curr = head
    while curr.next and data > curr.next.data:
        curr = curr.next
    curr.next = push(curr.next, data)
    return head

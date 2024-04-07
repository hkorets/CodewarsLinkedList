class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head and head.next:
        node = reverse(head.next)
        head.next.next = head
        head.next = None
        return node
    return head

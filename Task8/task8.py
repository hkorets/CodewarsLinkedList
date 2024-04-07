class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    curr = head
    while head:
        while head.next and head.data == head.next.data:
            head.next = head.next.next
        head = head.next
    return curr

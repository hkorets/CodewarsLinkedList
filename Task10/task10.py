class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    node = head.next
    node.next
    splited = Context(head, node)
    while node:
        head.next, head, node = node.next, node, node.next
    return splited

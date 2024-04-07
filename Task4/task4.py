from preloaded import Node

def get_nth(node, index):
    lst = []
    curr = node
    while curr != None:
        lst.append(curr.data)
        curr = curr.next
    if len(lst) + 1 < index or index < 0:
        raise IndexError
    return Node(lst[index])

from preloaded import Node

def swap_pairs(head):
    curr = Node(0)
    curr.next = head
    pr = curr
    while pr.next and pr.next.next:
        f = pr.next
        s = pr.next.next
        pr.next = s
        f.next = s.next
        s.next = f
        pr = f
    return curr.next

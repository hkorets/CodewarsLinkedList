def loop_size(node):
    counter = 1
    t = node
    h = node
    while True:
        t = t.next.next
        h = h.next
        if t == h:
            break
    h = h.next
    while h != t:
        counter += 1
        h = h.next
    return counter

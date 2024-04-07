def stringify(node):
    s = ''
    curr = node
    if node is None:
        return "None"
    while curr:
        s += str(curr.data)
        if curr.next:
            s += " -> "
        curr = curr.next
    s += " -> None"
    return s

def linked_list_from_string(s):
    lst = s.split(" -> ")[:-1][::-1]
    if not lst:
        return None
    curr = Node(int(lst[0]))
    for i in lst[1:]:
        new_node = Node(int(i), curr)
        curr = new_node
    return curr

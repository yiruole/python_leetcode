class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_intersect_node(head1, head2):
    if not head1 or not head2:
        return None

    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)

    if not loop1 and not loop2:
        return no_loop(head1, head2)
    if loop1 and loop2:
        return both_loop(head1, loop1, head2, loop2)

    return None

def get_loop_node(head):
    if not head or not head.next or not head.next.next:
        return None

    slow = head.next
    fast = head.next.next

    while slow != fast:
        if not fast.next or not fast.next.next:
            return None
        fast = fast.next.next
        slow = slow.next

    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

def no_loop(head1, head2):
    if not head1 or not head2:
        return None

    cur1, cur2 = head1, head2
    len1, len2 = 0, 0

    while cur1.next:
        len1 += 1
        cur1 = cur1.next

    while cur2.next:
        len2 -= 1
        cur2 = cur2.next

    if cur1 != cur2:
        return None

    cur1, cur2 = (head1, head2) if len1 > len2 else (head2, head1)
    for _ in range(abs(len1 - len2)):
        cur1 = cur1.next

    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1

def both_loop(head1, loop1, head2, loop2):
    if loop1 == loop2:
        cur1, cur2 = head1, head2
        len1, len2 = 0, 0

        while cur1 != loop1:
            len1 += 1
            cur1 = cur1.next

        while cur2 != loop2:
            len2 -= 1
            cur2 = cur2.next

        cur1, cur2 = (head1, head2) if len1 > len2 else (head2, head1)
        for _ in range(abs(len1 - len2)):
            cur1 = cur1.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur1

    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        return None

def main():
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next  # 8->6
    print(get_intersect_node(head1, head2).value)

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next = head1.next.next.next  # 7->4

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next  # 8->2
    print(get_intersect_node(head1, head2).value)

    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next  # 8->6
    print(get_intersect_node(head1, head2).value)

if __name__ == "__main__":
    main()
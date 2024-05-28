import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None

def reverse_linked_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

def reverse_double_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next
    return pre

def test_reverse_linked_list(head):
    if head is None:
        return None
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
    nodes[0].next = None
    N = len(nodes)
    for i in range(1, N):
        nodes[i].next = nodes[i - 1]
    return nodes[N - 1]

def test_reverse_double_list(head):
    if head is None:
        return None
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
    nodes[0].next = None
    pre = nodes[0]
    N = len(nodes)
    for i in range(1, N):
        cur = nodes[i]
        cur.last = None
        cur.next = pre
        pre.last = cur
        pre = cur
    return nodes[N - 1]

def generate_random_linked_list(len, value):
    size = random.randint(0, len)
    if size == 0:
        return None
    size -= 1
    head = Node(random.randint(0, value))
    pre = head
    while size != 0:
        cur = Node(random.randint(0, value))
        pre.next = cur
        pre = cur
        size -= 1
    return head

def generate_random_double_list(len, value):
    size = random.randint(0, len)
    if size == 0:
        return None
    size -= 1
    head = DoubleNode(random.randint(0, value))
    pre = head
    while size != 0:
        cur = DoubleNode(random.randint(0, value))
        pre.next = cur
        cur.last = pre
        pre = cur
        size -= 1
    return head

def get_linked_list_origin_order(head):
    ans = []
    while head is not None:
        ans.append(head.value)
        head = head.next
    return ans

def check_linked_list_reverse(origin, head):
    for i in range(len(origin) - 1, -1, -1):
        if origin[i] != head.value:
            return False
        head = head.next
    return True

def get_double_list_origin_order(head):
    ans = []
    while head is not None:
        ans.append(head.value)
        head = head.next
    return ans

def check_double_list_reverse(origin, head):
    end = None
    for i in range(len(origin) - 1, -1, -1):
        if origin[i] != head.value:
            return False
        end = head
        head = head.next
    for i in range(len(origin)):
        if origin[i] != end.value:
            return False
        end = end.last
    return True

def main():
    len = 50
    value = 100
    test_time = 10
    print("test begin!")
    for _ in range(test_time):
        node1 = generate_random_linked_list(len, value)
        list1 = get_linked_list_origin_order(node1)
        node1 = reverse_linked_list(node1)
        if not check_linked_list_reverse(list1, node1):
            print("Oops1!")

        node2 = generate_random_linked_list(len, value)
        list2 = get_linked_list_origin_order(node2)
        node2 = test_reverse_linked_list(node2)
        if not check_linked_list_reverse(list2, node2):
            print("Oops2!")

        node3 = generate_random_double_list(len, value)
        list3 = get_double_list_origin_order(node3)
        node3 = reverse_double_list(node3)
        if not check_double_list_reverse(list3, node3):
            print("Oops3!")

        node4 = generate_random_double_list(len, value)
        list4 = get_double_list_origin_order(node4)
        node4 = test_reverse_double_list(node4)
        if not check_double_list_reverse(list4, node4):
            print("Oops4!")

    print("test finish!")

if __name__ == "__main__":
    main()

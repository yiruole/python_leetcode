from collections import deque
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_serial(head):
    ans = deque()
    pres(head, ans)
    return ans

def pres(head, ans):
    if head is None:
        ans.append(None)
    else:
        ans.append(head.value)
        pres(head.left, ans)
        pres(head.right, ans)

def pos_serial(head):
    ans = deque()
    poss(head, ans)
    return ans

def poss(head, ans):
    if head is None:
        ans.append(None)
    else:
        poss(head.left, ans)
        poss(head.right, ans)
        ans.append(head.value)

def level_serial(head):
    ans = deque()
    if head is None:
        ans.append(None)
    else:
        ans.append(head.value)
        queue = deque([head])
        while queue:
            head = queue.popleft()
            if head.left:
                ans.append(head.left.value)
                queue.append(head.left)
            else:
                ans.append(None)
            if head.right:
                ans.append(head.right.value)
                queue.append(head.right)
            else:
                ans.append(None)
    return ans

def build_by_pre_queue(prelist):
    if not prelist or len(prelist) == 0:
        return None
    return preb(prelist)

def preb(prelist):
    value = prelist.popleft()
    if value is None:
        return None
    head = Node(value)
    head.left = preb(prelist)
    head.right = preb(prelist)
    return head

def build_by_pos_queue(poslist):
    if not poslist or len(poslist) == 0:
        return None
    stack = []
    while poslist:
        stack.append(poslist.popleft())
    return posb(stack)

def posb(posstack):
    value = posstack.pop()
    if value is None:
        return None
    head = Node(value)
    head.right = posb(posstack)
    head.left = posb(posstack)
    return head

def build_by_level_queue(level_list):
    if not level_list or len(level_list) == 0:
        return None
    head = generate_node(level_list.popleft())
    queue = deque()
    if head:
        queue.append(head)
    while queue:
        node = queue.popleft()
        node.left = generate_node(level_list.popleft())
        node.right = generate_node(level_list.popleft())
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return head

def generate_node(val):
    if val is None:
        return None
    return Node(val)

def generate_random_bst(max_level, max_value):
    return generate(1, max_level, max_value)

def generate(level, max_level, max_value):
    if level > max_level or random.random() < 0.5:
        return None
    head = Node(int(random.random() * max_value))
    head.left = generate(level + 1, max_level, max_value)
    head.right = generate(level + 1, max_level, max_value)
    return head

def is_same_value_structure(head1, head2):
    if head1 is None and head2 is not None:
        return False
    if head1 is not None and head2 is None:
        return False
    if head1 is None and head2 is None:
        return True
    if head1.value != head2.value:
        return False
    return is_same_value_structure(head1.left, head2.left) and is_same_value_structure(head1.right, head2.right)

def print_tree(head):
    print("Binary Tree:")
    print_in_order(head, 0, "H", 17)
    print()

def print_in_order(head, height, to, length):
    if head is None:
        return
    print_in_order(head.right, height + 1, "v", length)
    val = to + str(head.value) + to
    len_m = len(val)
    len_l = (length - len_m) // 2
    len_r = length - len_m - len_l
    val = get_space(len_l) + val + get_space(len_r)
    print(get_space(height * length) + val)
    print_in_order(head.left, height + 1, "^", length)

def get_space(num):
    return " " * num

if __name__ == "__main__":
    max_level = 5
    max_value = 100
    test_times = 1000
    print("test begin")
    for _ in range(test_times):
        head = generate_random_bst(max_level, max_value)
        pre = pre_serial(head)
        pos = pos_serial(head)
        level = level_serial(head)
        pre_build = build_by_pre_queue(deque(pre))
        pos_build = build_by_pos_queue(deque(pos))
        level_build = build_by_level_queue(deque(level))
        if not (is_same_value_structure(pre_build, pos_build) and is_same_value_structure(pos_build, level_build)):
            print("Oops!")
    print("test finish!")

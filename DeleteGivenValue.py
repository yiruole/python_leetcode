class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

def remove_value(head, num):
    # 移动 head 到第一个不需要删除的位置
    while head is not None and head.value == num:
        head = head.next
    
    # 当前链表的头结点可能已经是要删除的值，所以我们需要更新 head
    if head is None:
        return None
    
    pre = head
    cur = head.next
    
    while cur is not None:
        if cur.value == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    
    return head

# 用于测试
def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur.value, end=" -> ")
        cur = cur.next
    print("None")

# 创建一个链表 1 -> 2 -> 3 -> 2 -> 4 -> 2 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)

print("原始链表:")
print_linked_list(head)

head = remove_value(head, 2)

print("删除值为 2 后的链表:")
print_linked_list(head)

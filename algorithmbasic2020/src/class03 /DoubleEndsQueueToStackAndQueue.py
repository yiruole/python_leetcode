class Node:
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None

class DoubleEndsQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_from_head(self, value):
        cur = Node(value)
        if self.head is None:
            self.head = cur
            self.tail = cur
        else:
            cur.next = self.head
            self.head.last = cur
            self.head = cur

    def add_from_bottom(self, value):
        cur = Node(value)
        if self.head is None:
            self.head = cur
            self.tail = cur
        else:
            cur.last = self.tail
            self.tail.next = cur
            self.tail = cur

    def pop_from_head(self):
        if self.head is None:
            return None
        cur = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            cur.next = None
            self.head.last = None
        return cur.value

    def pop_from_bottom(self):
        if self.head is None:
            return None
        cur = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.last
            self.tail.next = None
            cur.last = None
        return cur.value

    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.queue = DoubleEndsQueue()

    def push(self, value):
        self.queue.add_from_head(value)

    def pop(self):
        return self.queue.pop_from_head()

    def is_empty(self):
        return self.queue.is_empty()

class MyQueue:
    def __init__(self):
        self.queue = DoubleEndsQueue()

    def push(self, value):
        self.queue.add_from_head(value)

    def poll(self):
        return self.queue.pop_from_bottom()

    def is_empty(self):
        return self.queue.is_empty()

def is_equal(o1, o2):
    if o1 is None and o2 is not None:
        return False
    if o1 is not None and o2 is None:
        return False
    if o1 is None and o2 is None:
        return True
    return o1 == o2

import random
from collections import deque

def main():
    one_test_data_num = 10
    value = 10
    test_times = 10

    for _ in range(test_times):
        my_stack = MyStack()
        my_queue = MyQueue()
        stack = []
        queue = deque()

        for _ in range(one_test_data_num):
            num_stack = random.randint(0, value)
            if not stack:
                my_stack.push(num_stack)
                stack.append(num_stack)
            else:
                if random.random() < 0.5:
                    my_stack.push(num_stack)
                    stack.append(num_stack)
                else:
                    if not is_equal(my_stack.pop(), stack.pop()):
                        print("oops!")

            num_queue = random.randint(0, value)
            if not queue:
                my_queue.push(num_queue)
                queue.append(num_queue)
            else:
                if random.random() < 0.5:
                    my_queue.push(num_queue)
                    queue.append(num_queue)
                else:
                    if not is_equal(my_queue.poll(), queue.popleft()):
                        print("oops!")

    print("finish!")

if __name__ == "__main__":
    main()

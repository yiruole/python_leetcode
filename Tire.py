import random
import string

class Trie:
    class Node:
        def __init__(self):
            self.pass_count = 0
            self.end_count = 0
            self.nexts = [None] * 26

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        if not word:
            return
        node = self.root
        node.pass_count += 1
        for char in word:
            path = ord(char) - ord('a')
            if node.nexts[path] is None:
                node.nexts[path] = self.Node()
            node = node.nexts[path]
            node.pass_count += 1
        node.end_count += 1

    def erase(self, word):
        if self.count_words_equal_to(word) != 0:
            node = self.root
            node.pass_count -= 1
            for char in word:
                path = ord(char) - ord('a')
                node.nexts[path].pass_count -= 1
                if node.nexts[path].pass_count == 0:
                    node.nexts[path] = None
                    return
                node = node.nexts[path]
            node.end_count -= 1

    def count_words_equal_to(self, word):
        if not word:
            return 0
        node = self.root
        for char in word:
            path = ord(char) - ord('a')
            if node.nexts[path] is None:
                return 0
            node = node.nexts[path]
        return node.end_count

    def count_words_starting_with(self, prefix):
        if not prefix:
            return 0
        node = self.root
        for char in prefix:
            path = ord(char) - ord('a')
            if node.nexts[path] is None:
                return 0
            node = node.nexts[path]
        return node.pass_count

# 暴力方法实现
class BruteForceTrie:
    def __init__(self):
        self.words = []

    def insert(self, word):
        self.words.append(word)

    def erase(self, word):
        if word in self.words:
            self.words.remove(word)

    def count_words_equal_to(self, word):
        return self.words.count(word)

    def count_words_starting_with(self, prefix):
        return sum(1 for word in self.words if word.startswith(prefix))

# 生成随机测试用例
def generate_random_string(max_length):
    length = random.randint(1, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# 对数器测试
def main():
    test_times = 1000
    max_length = 10
    operations = ['insert', 'erase', 'count_words_equal_to', 'count_words_starting_with']
    succeed = True

    for _ in range(test_times):
        trie = Trie()
        brute_trie = BruteForceTrie()

        for _ in range(100):  # 每个测试用例进行100次操作
            op = random.choice(operations)
            word = generate_random_string(max_length)

            if op == 'insert':
                trie.insert(word)
                brute_trie.insert(word)
            elif op == 'erase':
                trie.erase(word)
                brute_trie.erase(word)
            elif op == 'count_words_equal_to':
                if trie.count_words_equal_to(word) != brute_trie.count_words_equal_to(word):
                    succeed = False
                    print(f"Failed on operation {op} with word {word}")
                    break
            elif op == 'count_words_starting_with':
                if trie.count_words_starting_with(word) != brute_trie.count_words_starting_with(word):
                    succeed = False
                    print(f"Failed on operation {op} with prefix {word}")
                    break

        if not succeed:
            break

    print("Nice!" if succeed else "Failed!")

if __name__ == "__main__":
    main()

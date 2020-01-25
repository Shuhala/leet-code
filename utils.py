from collections import deque

import big_o


def estimate_big_o(func, generator, **kwargs):
    """
    Integers:
        generator = lambda n: big_o.datagen.integers(n, 0, 10000)
    List integers:
        generator = lambda n: big_o.datagen.range_n(n, 1)
    """
    best, others = big_o.big_o(func, generator, **kwargs)
    print(best)


def print_tree(root):
    buf = deque()
    output = []
    if not root:
        print('$')
    else:
        buf.append(root)
        count, next_count = 1, 0
        while count:
            node = buf.popleft()
            if node:
                output.append(node.val)
                count -= 1
                for n in (node.left, node.right):
                    if n:
                        buf.append(n)
                        next_count += 1
                    else:
                        buf.append(None)
            else:
                output.append('$')
            if not count:
                print(output)
                output = []
                count, next_count = next_count, 0
        # print the remaining all empty leaf node part
        output.extend(['$'] * len(buf))
        print(output)

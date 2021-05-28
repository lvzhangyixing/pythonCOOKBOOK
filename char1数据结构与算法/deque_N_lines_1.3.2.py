# 匹配文件中的python,并通过
# dequeue输出最后检查过的N行文本
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # 返回当前行，以及最后检查的N行队列
            yield line, previous_lines
        previous_lines.append(line)


# Example use on file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        # 没匹配到一次，输出一次匹配行和最后N行队列
        for line, prevlines in search(f, 'Python', 5):
            # 循环读取返回的的最后N行队列prevlines
            for pline in prevlines:
                print(pline, end='')
            # 输出匹配行
            print(line, end='')
            print('-' * 20)

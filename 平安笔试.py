# 1. 写出自己熟悉的单例模式代码,并说明其应用场景
class Simple(object):
    _instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Simple, cls).__new__(cls)
        return cls._instance


# 应用场景： 主要用在创建redis、mysql、rabbitmq等链接

# 2. 写一个快速排序

def mid(seq, l, r):
    i = l - 1
    for j in range(l, r):
        if seq[j] <= seq[r]:
            i += 1
            seq[i], seq[j] = seq[j], seq[i]
    seq[i + 1], seq[r] = seq[r], seq[i + 1]
    return i


def quicksort(seq, l, r):
    if l < r:
        mid_num = mid(seq, l, r)
        quicksort(seq, l, mid_num)
        quicksort(seq, mid_num + 1, r)


seq = [2, 5, 8, 4, 6, 1, 9, 3]
quicksort(seq, 0, len(seq) - 1)
print(seq)

# 3. 处理sample.txt,并按要求输出结果
# sample.txt内容如下
# $ cat sample.txt
# ID, col
# 1 abc
# 1 abc
# 2 def
# 5 dga
# 5 dga
# 5 def

# 要求输出结果如下
# 1 abc: 2
# 2 def: 1
# 5 dga: 2
# 5 def: 1
from collections import Counter

with open('sample.txt', 'r') as f:
    content = [line.rstrip('\n') for line in f]
    content = content[1:]
    result = Counter(content)
    for i in result:
        print(F"{i} {result[i]}")

# 4. 地上有一个m行n列的方格,从坐标[0, 0]到坐标[m-1, n-1].一个机器人从坐标[0, 0]的格子开始移动,他每次可以向左/右/上/下移动1格(不能移动到方格区域外),也不能进入行坐标和列坐标的各数位数字之和大于k的格子,例如,当k为18时,机器人能够进入方格[35, 37],因为3+5+3+7=18,但它不能进入[35, 38]的格子,因为3+5+3+8=19,请问该机器人能够到达多少个格子?
# 示例:
# 输入: m=2, n=3, k=1
# 输出: 3
# 提示:
#   1<=n,m<=100
#   0<=k<=20

m = 2
n = 3
k = 1
total = 1  # 起始格


def sum(x):
    a = x % 10
    b = x // 10
    return a + b


for i in range(m - 1):
    for j in range(n - 1):
        if sum(i) + sum(j) <= k:
            total += 1
print(F"能够到达 {total} 个格子")

# 5. 全局变量num=1，通过两个线程循环输出该变量1到100
# 例如:
# Thread1: 1
# Thread2: 2
# Thread1: 3
# Thread2: 4
# Thread1: 5

import threading

num = 1


def thread_a():
    global num
    while num <= 100:
        if num % 2 == 0:
            continue
        else:
            lock_b.acquire()
            print(num),
            num += 1
            lock_a.release()


def thread_b():
    global num
    while num <= 100:
        if num % 2 != 0:
            continue
        else:
            lock_a.acquire()
            print(num),
            num += 1
            lock_b.release()


lock_a = threading.Lock()
lock_b = threading.Lock()

ta = threading.Thread(None, thread_a)
tb = threading.Thread(None, thread_b)

lock_a.acquire()

ta.start()
tb.start()
ta.join()
tb.join()

# 6. 尽可能多的写出你所知道的linux命令(可以不写相关参数,数量不限,越多越好)
# source
# vi
# cat
# more
# less
# tail
# df
# du
# top
# ps
# grep
# cp
# mv
# touch
# mkdir
# pwd
# tar
# echo
# rm

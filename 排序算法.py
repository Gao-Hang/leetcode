# https://baijiahao.baidu.com/s?id=1635285231673698375&wfr=spider&for=pc
# 冒泡排序
# 冒泡排序时间复杂度On2/先假设a[0]最小，遍历后面元素，有小的则替换，依次确定a[2]～a[n]的数据
def bubble_sort(arr, l):
    for i in range(l):
        for j in range(l - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

seq = [2, 8, 7, 1, 3, 5, 6, 4]
bubble_sort(seq, len(seq) - 1)
print(seq)

# 快速排序：
# https://blog.csdn.net/u011213419/article/details/81053629
def quicksort(seq, l, r):
    if l < r:
        m = partion(seq, l, r)
        quicksort(seq, l, m)
        quicksort(seq, m + 1, r)


def partion(seq, l, r):
    i = l - 1
    for j in range(l, r):
        if seq[j] <= seq[r]:
            i += 1
            seq[i], seq[j] = seq[j], seq[i]
            print('+', seq, '+')
    seq[i + 1], seq[r] = seq[r], seq[i + 1]
    return i


seq = [2, 8, 7, 1, 3, 5, 6, 4]
quicksort(seq, 0, len(seq) - 1)
print(seq)

# fib
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


# 插入排序

a = 2
print(fib(a))
import numpy as np

amount= 1.6
amount= 500

def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
                if value[i][j] == amount:
                    return i, j, value, True

    return 0, 0, value, False


def show(value, i, j):
    """
    反向推导背包状态转移矩阵value[i,j]对应的组合
    """
    x = [0 for i in range(i)]
    j = j
    for i in range(i, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = 1
            j = j - 1
    return [k for k in range(len(x)) if x[k] == 1]


if __name__ == '__main__':
    n = 6
    c = 6
    w = [1, 1, 1, 1, 1, 1]
    # 金额从小到大排列
    v = [10, 300, 0.5, 200, 1, 1]
    # v = [0.5,1,1,10, 200, 300]
    # v = [0.1, 0.2, 0.2, 0.2, 0.5, 1]
    i, j, value, boolValue = bag(n, c, w, v)
    for x in value:
        print(x)
    if not boolValue:
        arr = np.array(value)
        arr[arr > amount] = 0
        index = int(arr.argmax())
        m, n = arr.shape
        i = int(index / n)
        j = index % n
        for p in arr:
            print(p)
    print(i, j)
    print(show(value,i, j))


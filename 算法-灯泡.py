import random

i = 0
j = []  # 100个灯泡
while True:
    '''创建100个灯泡'''
    if i == 100:
        break
    k = ['亮', '暗']
    k = random.sample(k, 1)
    j.append(k)
    i += 1
print(j)
j[0] = ['亮']  # 选择一个亮灯泡，标记为0号
m, n = 0, 0
while True:
    m, s, n = m + 1, m + 2, m + 3

    if n == 100:
        if j[m] == ['暗']:
            j[m] = ['亮']
        break
    if j[m] == ['暗']:
        j[m] = ['亮']
        if j[s] == ['暗'] and j[n] == ['暗']:
            j[s] = ['亮']
            j[n] = ['亮']

        elif j[s] == ['亮'] and j[n] == ['暗']:
            j[s] = ['暗']
            j[n] = ['亮']

        elif j[s] == ['暗'] and j[n] == ['亮']:
            j[s] = ['亮']
            j[n] = ['暗']

        else:
            j[s] = ['暗']
            j[n] = ['暗']
print(j)

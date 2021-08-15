def jump(n):
    if n == 1:
        return n
    return 2 * jump(n - 1)


if __name__ == "__main__":
    print(jump(3))
#
#
def find():
    for thief in ['a', 'b', 'c', 'd']:
        # != 可替换为 is not ,   == 替换为 is
        result = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief != 'd')
        if result == 3:
            return thief


if __name__ == "__main__":
    res = find()
    print(F"小偷是：{res}")

# class Parent(object):
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)
#
# a = [1, 2, 3, [4, 5, 6, ], 7, 8]
# a[3][2] = 100
# print(a)
# a[2] = 100
# print(a)
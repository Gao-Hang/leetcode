class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        st = str(x)
        li = list(st)
        if li[0] == '-':
            a = li.pop(0)
            li.reverse()
            li.insert(0, a)
            rest = "".join(li)
            answer = int(rest)
            if answer < (-2) ** 31:
                return 0
            return answer
        else:
            li.reverse()
            rest = "".join(li)
            answer = int(rest)
            if answer > (2 ** 31 - 1):
                return 0
            return answer


if __name__ == '__main__':
    x = "-123"
    c = Solution().reverse(x)
    print(c)

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#  示例 2:
#
# 输入: -123
# 输出: -321
#
# 示例 3:
#
# 输入: 120
# 输出: 21

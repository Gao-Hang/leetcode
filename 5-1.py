class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, maxl = 0, 0
        for i in range(len(s)):
            if i - maxl >= 1 and s[i - maxl - 1:i + 1] == s[i - maxl - 1:i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
            if i - maxl >= 0 and s[i - maxl:i + 1] == s[i - maxl:i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start:start + maxl]

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

if __name__ == '__main__':
    a = 'babad'
    c = Solution().longestPalindrome(a)
    print(c)

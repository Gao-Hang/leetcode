class Solution:
    def lengthOfLongestSubstring(self, s):
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


class Solution1:
    def lengthOfLongestSubstring1(self, s):
        max = 0
        number = 0
        test = ''
        for i in s:
            if i not in test:
                test += i
                number += 1
            else:
                if number >= max:
                    max = number
                index = test.index(i)
                test = test[(index+1):] + i
                number = len(test)
        if number > max:
            max = number
        return max


class Solution2:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max = ""
        test = ""
        for ch in s:
            if ch in test:
                if len(test) > len(max):
                    max = test
                test = test[test.index(ch) + 1:] + ch
            else:
                test += ch
        return max(len(max), len(test))


class Solution3:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


if __name__ == '__main__':
    s1 = "pwwkew"
    s2 = "pwwkew"
    a = Solution().lengthOfLongestSubstring(s1)
    b = Solution1().lengthOfLongestSubstring1(s1)
    print(a)
    print(b)

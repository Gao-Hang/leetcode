class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        a.sort()
        if len(a) % 2 == 0:
            i = int(len(a) / 2)
            return float((a[i] + a[i - 1]) / 2)
        else:
            i = int(len(a) / 2) + 1
            return float(a[i - 1])


# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是 (2 + 3)/2 = 2.5

if __name__ == '__main__':
    a = [1, 2]
    b = [3, 4]
    c = Solution().findMedianSortedArrays(a, b)
    print(c)

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            # a=i
            # b=nums[i]
            # c=nums[i-1]
            nums[i] = nums[i] + max(nums[i - 1], 0)
            # 思想是动态规划，nums[i-1]并不是数组前一项的意思，
            # 而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。
            # 如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
            # d=nums[i]
            # r=nums
            # t=1
        return max(nums)


if __name__ == '__main__':
    x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    x = [1, 2, 7, -1, -4, 11]
    x = [-5, -1, -3, -4, -6]
    c = Solution().maxSubArray(x)
    print(c)

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# V(i,j)=min(V(i-1,j),V(i,j-1))+(i,j)
# V(0,0)=(0,0)
# V(i,0)=V(i-1,0),+(i,0)
# V(0,j)=V(0,j-1)+(0,j)


class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[-1 for j in range(n)] for i in range(m)]
        # 此数组用于记忆化搜索
        dp = [[0] * len(grid[0]) for i in range(len(grid))]

        for i in range(m):
            for j in range(n):
                # 在起点的时候

                if i == j == 0:
                    dp[0][0] = grid[0][0]

                # 在左边缘的时候
                elif i != 0 and j == 0:
                    dp[i][0] = dp[i - 1][0] + grid[i][0]

                # 在上边缘的时候
                elif i == 0 and j != 0:
                    dp[0][j] = dp[0][j - 1] + grid[0][j]
                # 普遍情况下
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        a=dp

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    x = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    c = Solution().minPathSum(x)
    print(c)

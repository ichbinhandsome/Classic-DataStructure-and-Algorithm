class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)+1
        n = len(word2)+1
        
        dp = [[0]*m for j in range(n)]
        for i in range(1,m):
            dp[0][i] = i
        for j in range(1,n):
            dp[j][0] = j  
        for i in range(1,n):
            for j in range(1,m):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    
        return dp[-1][-1]

        # m, n = len(word1)+1, len(word2)+1
        # # dp = [[0]*m for i in range(n)]
        # dp = [[0]*n for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             dp[i][j] = max(i,j)
        #         else:
        #             if word1[i-1] == word2[j-1]:
        #                 dp[i][j] = dp[i-1][j-1]
        #             else:
        #                 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        # print(dp)
        # return dp[-1][-1]
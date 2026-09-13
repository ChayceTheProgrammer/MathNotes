"""
Original Question:
Determine an LCS of X = ⟨R, H, U, B, A, R, B⟩ and
Y = ⟨S, T, R, A, W, B, E, R, R, Y ⟩ using the dynamic programming algorithm
that was discussed in class. Make sure that you explain your answer step-by-
step, in detail, rather than just giving an LCS. [Make sure that you list X
vertically, and Y horizontally when constructing the table. If xi = yj , and
c[i − 1, j] = c[i, j − 1], choose c[i − 1, j]. Explain row-by-row how the table is
constructed.]
Why do we care? For every algorithm, you should make sure that you can work
it out step-by-step.
"""

#LeetCode Submission:
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # Characters match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Characters do not match

    # The length of the longest common subsequence will be in dp[m][n]
    return dp[m][n]

if __name__ == '__main__':
    # Example usage
    text1 = "abcde"
    text2 = "ace"
    print(longestCommonSubsequence(text1, text2))  # Output: 3

    text1 = "abc"
    text2 = "abc"
    print(longestCommonSubsequence(text1, text2))  # Output: 3

    text1 = "abc"
    text2 = "def"
    print(longestCommonSubsequence(text1, text2))  # Output: 0

    #testing HW5 Problem 1
    text1 = "RHUBARB"
    text2 = "STRAWBERRY"
    print(longestCommonSubsequence(text1, text2))


def lcs(s1, s2):
    """
    Finds the longest common subsequence between two strings and returns the sequence.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        str: The longest common subsequence.
    """
    m, n = len(s1), len(s2)

    # Create a 2D array to store the lengths of the LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Create a 2D array to store the direction of the path
    # 0: diagonal, 1: up, 2: left
    direction = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table and the direction table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direction[i][j] = 0
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    direction[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1]
                    direction[i][j] = 2

    # Reconstruct the longest common subsequence
    i, j = m, n
    lcs_str = ""
    while i > 0 and j > 0:
        if direction[i][j] == 0:
            lcs_str = s1[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif direction[i][j] == 1:
            i -= 1
        else:
            j -= 1

    return lcs_str

s1 = "RHUBARB"
s2 = "STRAWBERRY"
print(lcs(s1, s2))  # Output: "ADH"
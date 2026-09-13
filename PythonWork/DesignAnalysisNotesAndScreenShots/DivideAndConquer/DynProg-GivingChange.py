
def make_change(coins, amount):
    """
    Finds the minimum number of coins needed to make
    the given amount using the provided coin denominations.
    How the algorithm works:

    We initialize a list dp to store the minimum number of coins needed to make each amount from 0 to the target amount.
    We set the base case, where the minimum number of coins needed to make 0 cents is 0.
    We then iterate through the amounts from 1 to the target amount.
    For each amount, we iterate through the available coin denominations.
    If the current coin value is less than or equal to the current amount, we update the minimum number of coins needed for the current amount by taking the minimum of the current value in dp[i] and the minimum number of coins needed for the amount i - coin plus 1 (for the current coin).
    Finally, we return the minimum number of coins needed to make the target amount, or -1 if it's not possible.
    This algorithm has a time complexity of O(amount * len(coins)), as we iterate through all the amounts and all the coin denominations.

    Args:
        coins (list): A list of coin denominations.
        amount (int): The target amount to make change for.

    Returns:
        int: The minimum number of coins needed to make the given amount.
    """
    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins are needed to make 0 amount
    dp[0] = 0

    # Iterate through the amounts from 1 to the target amount
    for i in range(1, amount + 1):
        # Iterate through the available coin denominations
        for coin in coins:
            # If the current coin value is less than or equal to the current amount
            if coin <= i:
                # Update the minimum number of coins needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If it's not possible to make the target amount, return -1
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = 15
    min_coins = make_change(coins, amount)
    print(f"The minimum number of coins needed to make {amount} cents is {min_coins}.")
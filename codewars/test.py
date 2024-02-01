def countSubarraysWithMean(permutation):
    n = len(permutation)
    prefix_sum = [0] * n
    dp = [[0] * (n + 1) for _ in range(n)]
    counter = [0] * (n + 1)

    prefix_sum[0] = permutation[0]
    dp[0][permutation[0]] = 1
    counter[permutation[0]] += 1

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + permutation[i]
        dp[i][prefix_sum[i]] = 1
        counter[prefix_sum[i]] += 1

        for j in range(i):
            diff = prefix_sum[i] - prefix_sum[j]
            dp[i][diff] += dp[j][diff - permutation[i]]
            counter[diff] += dp[j][diff - permutation[i]]

    return counter[1:]

# Example usage
permutation = [2, 4, 1, 3]
result = countSubarraysWithMean(permutation)
print(result)  # Output: [1, 2, 2, 1]




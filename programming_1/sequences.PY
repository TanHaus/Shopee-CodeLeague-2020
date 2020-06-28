N, M, K = [int(x) for x in input().split()]


def foo(i, j):
    return A[i] * j*j + B[i]


A = {}
B = {}
C = {}
mod_arr = []
for i in range(N):
    A[i + 1], B[i + 1], C[i + 1] = [int(x) for x in input().split()]
    for j in range(C[i + 1]):
        mod_arr.append(foo(i + 1, j + 1))
print(mod_arr)

l = len(mod_arr)
mod_arr

def sumSubSequence(arr, length, m):
        # Find sum pf array elements
    summ = 0
    for i in arr:
        summ += i

    # dp[i][j] would be > 0 if arr[0..i-1] has
    # a subsequence with sum equal to j.
    dp = [[0 for i in range(summ + 1)]
          for j in range(length + 1)]

    # There is always sum equals zero
    for i in range(length + 1):
        dp[i][0] += 1

    # Fill up the dp table
    for i in range(1, length + 1):
        dp[i][arr[i - 1]] += 1
        for j in range(1, summ + 1):
            if dp[i - 1][j] > 0:
                dp[i][j] += 1
                dp[i][j + arr[i - 1]] += 1

    # Initialize the counter
    count = 0
    for i in range(1, summ + 1):

        # Check if the sum exists
        if dp[length][i] > 0:

            # check sum is divisible by m
            if i % m == 0:
                count += dp[length][i]

    return count


print(sumSubSequence(mod_arr, len(mod_arr), K))

N, K = [int(x) for x in input().split()]

price_array = []
for i in range(N):
    price_array.append([int(x) for x in input().split()])

paired_sum = []
for i in range(N-1):
    sum_row = []
    for j in range(2):
        center = price_array[i][j]
        right = price_array[i][j + 1]
        bottom = price_array[i + 1][j]
        sum_row.append([center + right, center + bottom])
    paired_sum.append(sum_row)


# find largest sum
# if an overlap is among the largest sum, remove the either overlap and find the largest sum of the subset.
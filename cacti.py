def cacti_number(matrix):
    @functools.lru_cache(maxsize=None)
    def dp(i, j, prev):
        if i == len(matrix):
            return 0
        next_i = i + (j + 1) // len(matrix[0])
        next_j = (j + 1) % len(matrix[0])
        if matrix[i][j] == 1:
            return dp(next_i, next_j, 0)
        if prev == 1:
            return dp(next_i, next_j, 0)
        count = dp(next_i, next_j, 1) + 1
        if i < len(matrix) - 1 and j > 0 and matrix[i + 1][j - 1] == 1:
            return count
        return max(count, dp(next_i, next_j, 0))
    return dp(0, 0, 0)

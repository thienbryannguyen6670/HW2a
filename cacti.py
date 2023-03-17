def cacti_number(func):
    def wrapper(arr):
        rows, cols = len(arr), len(arr[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 0:
                    # Check all adjacent and diagonal positions for existing cacti
                    adj_cacti = 0
                    for r in range(max(0, i-1), min(rows, i+2)):
                        for c in range(max(0, j-1), min(cols, j+2)):
                            if arr[r][c] == 1:
                                adj_cacti += 1
                                break
                    if adj_cacti == 0:
                        count += 1
        return count
    return wrapper

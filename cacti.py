def count_cacti(plot):
    count = 0
    rows, cols = len(plot), len(plot[0])
    for i in range(rows):
        for j in range(cols):
                if i > 0 and plot[i-1][j] == 1:
                    adjacent = True
                elif i < rows-1 and plot[i+1][j] == 1:
                    adjacent = True
                elif j > 0 and plot[i][j-1] == 1:
                    adjacent = True
                elif j < cols-1 and plot[i][j+1] == 1:
                    adjacent = True
                # Check for adjacent cacti diagonally
                elif i > 0 and j > 0 and plot[i-1][j-1] == 1:
                    adjacent = True
                elif i > 0 and j < cols-1 and plot[i-1][j+1] == 1:
                    adjacent = True
                elif i < rows-1 and j > 0 and plot[i+1][j-1] == 1:
                    adjacent = True
                elif i < rows-1 and j < cols-1 and plot[i+1][j+1] == 1:
                    adjacent = True
                if not adjacent:
                    count += 1
    return count
def cacti_number(func):
    def wrapper(*args, **kwargs):
        plot = args[0]
        rows, cols = len(plot), len(plot[0])
        max_cacti = 0
        for i in range(rows):
            for j in range(cols):
                if plot[i][j] == 0:
                    adjacent = False
                    # Check for adjacent cacti horizontally and vertically
                    if i > 0 and plot[i-1][j] == 1:
                        adjacent = True
                    elif i < rows-1 and plot[i+1][j] == 1:
                        adjacent = True
                    elif j > 0 and plot[i][j-1] == 1:
                        adjacent = True
                    elif j < cols-1 and plot[i][j+1] == 1:
                        adjacent = True
                    # Check for adjacent cacti diagonally
                    elif i > 0 and j > 0 and plot[i-1][j-1] == 1:
                        adjacent = True
                    elif i > 0 and j < cols-1 and plot[i-1][j+1] == 1:
                        adjacent = True
                    elif i < rows-1 and j > 0 and plot[i+1][j-1] == 1:
                        adjacent = True
                    elif i < rows-1 and j < cols-1 and plot[i+1][j+1] == 1:
                        adjacent = True
                    if not adjacent:
                        test_plot = [row[:] for row in plot]
                    test_plot[i][j] = 1
                    cacti_count = count_cacti(test_plot)
                    if cacti_count > max_cacti:
                        max_cacti = cacti_count
            return func(*args, **kwargs), max_cacti
        return wrapper

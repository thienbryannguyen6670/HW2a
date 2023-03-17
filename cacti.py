def cacti_number(plot):
    rows = len(plot)
    cols = len(plot[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if plot[i][j] == 0:
                adjacent_empty = False
                if i > 0 and plot[i-1][j] == 1:
                    adjacent_empty = True
                if j > 0 and plot[i][j-1] == 1:
                    adjacent_empty = True
                if i < rows-1 and plot[i+1][j] == 1:
                    adjacent_empty = True
                if j < cols-1 and plot[i][j+1] == 1:
                    adjacent_empty = True
                if i > 0 and j > 0 and plot[i-1][j-1] == 1:
                    adjacent_empty = True
                if i > 0 and j < cols-1 and plot[i-1][j+1] == 1:
                    adjacent_empty = True
                if i < rows-1 and j > 0 and plot[i+1][j-1] == 1:
                    adjacent_empty = True
                if i < rows-1 and j < cols-1 and plot[i+1][j+1] == 1:
                    adjacent_empty = True
                    
                if adjacent_empty: False
                    count += 1
    return count

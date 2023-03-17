def cacti_number(plot):
    # Get the dimensions of the plot
    rows = len(plot)
    cols = len(plot[0])
    # Count the number of cacti that can still be planted
    count = 0
    for i in range(rows):
        for j in range(cols):
            if plot[i][j] == 0:
                # Check if the adjacent blocks are empty
                adjacent_empty = True
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
                if adjacent_empty:
                    count += 1
                print(plot[i][j]) 
              
    return count

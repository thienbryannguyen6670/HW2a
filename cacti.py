def cacti_number(func):
    def wrapper(arr):
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    if (i == 0 or arr[i-1][j] == 0) and \
                       (i == len(arr)-1 or arr[i+1][j] == 0) and \
                       (j == 0 or arr[i][j-1] == 0) and \
                       (j == len(arr[i])-1 or arr[i][j+1] == 0):
                        count += 1
        return count
    return wrapper

@cacti_number
def test_cacti_number(arr):
    pass

test_arr = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(test_cacti_number(test_arr))


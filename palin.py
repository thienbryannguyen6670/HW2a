def palindrome(lst):

    n = len(lst)
    for i in range(n // 2):
        if lst[i] != lst[n - i - 1]:
            return False
    return True

#assert palindrome([1, 2, "Espresso", "Madeline", 2, 1]) == False
#assert palindrome(['a', True, False, False, True, 'a']) == True
#assert palindrome([1, 2, 3, 4, 3, 2, 1]) == True
#assert palindrome(['hello', 'world']) == False
print("All test case pass")

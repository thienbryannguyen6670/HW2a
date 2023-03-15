test_list = [1,2, "Espresso", "Madeline", 2,1]

print ("The original list is : " +str(test_list))
reverse = test_list[::-1]
res = test_list == reverse
print("Is a Palindrome : " +str(res))

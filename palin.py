def isPalindrome(my_str):
   if my_str == my_str[::-1]:
    print("True")
   else:
    print("False")
        
my_list = [1,2,"Espresso","Madeline",2,1]

my_list = ' '.join([str(elem) for elem in my_list])
isPalindrome(my_list)

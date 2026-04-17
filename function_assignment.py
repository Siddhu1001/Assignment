#1. Write a Python function to find the maximum of three numbers.
# def max_n():
#     num=[10,20,30]
#     max_num=max(num)
#     return max_num
# print(max_n())


#2. Write a Python function to sum all the numbers in a list.
	# Sample List : (8, 2, 3, 0, 7)
	# Expected Output : 20
# def sum_l():
#     sample_list=[8,2,3,0,7]
#     print(sum(sample_list))
# sum_l()    

# 3. Write a Python function to multiply all the numbers in a list.
# 	Sample List : (8, 2, 3, -1, 7)
# 	Expected Output : -336

# def mul_list(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result
# sample = (8, 2, 3, -1, 7)
# print(mul_list(sample))

# 4. Write a Python function to reverse a string. 
# 	Sample String : "1234abcd"
# 	Expected Output : "dcba4321"

# def rev_str():
#     sample='123abcd'
#     print(sample[::-1])
# rev_str()

# 5. Write a Python function to check whether a number falls within a given range.
# def number_in_renge():
#     num=10
#     for i in range (1,20):
#         if num==10:
#             print("num in the list ")
#         else:
#             print("num not in range!!!")    
# number_in_renge()       




# 6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
	# Sample String : 'The quick Brow Fox'
	# Expected Output :
	# No. of Upper case characters : 3
	# No. of Lower case Characters : 12

# def count_case_letters(s):
#     upper = 0
#     lower = 0
#     for char in s:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#     print("No. of Upper case characters :", upper)
#     print("No. of Lower case Characters :", lower)
# sample_str = 'The quick Brow Fox'
# count_case_letters(sample_str)


	
# 7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# 	Sample List : [1,2,3,3,3,3,4,5]
# 	Unique List : [1, 2, 3, 4, 5]

# def unique_elements(lst):
#     return list(set(lst))
# print(unique_elements([1,2,3,3,3,3,4,5]))
	     
# 8. Write a Python function that checks whether a passed string is a palindrome or not.

# 	Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# def palindrome(s):
#     s = s.replace(" ", "").lower()
   
#     return s == s[::-1]
# print(palindrome("madam"))   


# 9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# 	Sample Items : green-red-yellow-black-white
# 	Expected Result : black-green-red-white-yellow

# def sort_hyphen(s):
#     words = s.split('-') 
#     words.sort()              
#     return '-'.join(words)    
# sample = "green-red-yellow-black-white"
# print(sort_hyphen(sample))

# def count_local_variables():
#     a = 10
#     b = 20
#     c = a + b
#     return len(locals())
# print(count_local_variables())


# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

# 	Sample Output:
# 	25
# 	48


# add_15 = lambda x: x + 15
# multiply = lambda x, y: x * y
# print(add_15(10))   
# print(multiply(6, 8)) 




# 12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# 	Sample Output:
# 	Double the number of 15 = 30
# 	Triple the number of 15 = 45
# 	Quadruple the number of 15 = 60
# 	Quintuple the number 15 = 75

# def multiplier(n):
#     return lambda x: x * n

# double = multiplier(2)
# triple = multiplier(3)
# quadruple = multiplier(4)
# quintuple = multiplier(5)

# num = 15
# print( double(num))
# print( triple(num))
# print( quadruple(num))
# print( quintuple(num))


# 13. Write a Python program to sort a list of tuples using Lambda.

# 	Original list of tuples:
# 	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# 	Sorting the List of Tuples:
# 	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# sorted_marks = sorted(marks, key=lambda x: x[1])
# print("Sorting the List of Tuples:")
# print(sorted_marks)

# 14. Write a Python program to sort a list of dictionaries using Lambda.

# 	Original list of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# 	Sorting the List of dictionaries :
# 	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
# Original list
# mobiles = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]

# sorted_mobiles = sorted(mobiles, key=lambda x: x['color'])

# print("Sorting the dict:")
# print(sorted_mobiles)


# 15. Write a Python program to filter a list of integers using Lambda.

# 	Original list of integers:
# 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	Even numbers from the said list:
# 	[2, 4, 6, 8, 10]
# 	Odd numbers from the said list:
# 	[1, 3, 5, 7, 9]	

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print("Even numbers:")
# print(even_numbers)
# print("Odd numbers:")
# print(odd_numbers)


# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.
# 	Original list of integers:
# 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 	Square every number of the said list:
# 	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 	Cube every number of the said list:
# 	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    
# def square_and_cube(numbers):
#     squares = list(map(lambda x: x**2, numbers))
#     cubes = list(map(lambda x: x**3, numbers))   
#     print("Square:")
#     print(squares)   
#     print("Cubet:")
#     print(cubes)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_and_cube(numbers)


# 18. Write a Python program to find if a given string starts with a given character using Lambda.

# def starts_char(string, ch):
#     check = lambda s: s.startswith(ch)
#     return check(string)

# print(starts_char("Python", "P")) 
# print(starts_char("Python", "p")) 


# 19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

# 	Original arrays:
# 	[-1, 2, -3, 5, 7, 8, 9, -10]
# 	Rearrange positive and negative numbers of the said array:
# 	[2, 5, 7, 8, 9, -10, -3, -1]

# def rearrange_numbers(arr):
#     return sorted(arr, key=lambda x: (x < 0, x))
# numbers = [-1, 2, -3, 5, 7, 8, 9, -10]
# print(rearrange_numbers(numbers))

# 20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

# 	Original arrays:
# 	[1, 2, 3, 5, 7, 8, 9, 10]
# 	Number of even numbers in the above array: 3
# 	Number of odd numbers in the above array: 5

# def count_even_odd(numbers):
#     even = sum(map(lambda x: x % 2 == 0, numbers))
#     odd = sum(map(lambda x: x % 2 != 0, numbers))
    
#     print("Even:", even)
#     print("Odd:", odd)


# 21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

# 	Orginal list:
# 	[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# 	Numbers of the above list divisible by nineteen or thirteen:
# 	[19, 65, 57, 39, 152, 190]

# def divisible(numbers):
#     result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
#     return result
# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# print(divisible(nums))



# 22. Write a Python program to check whether a given string contains a capital letter,
# a lower case letter, a number and a minimum length using lambda.

def check_string(s):
    return (any(map(lambda c: c.isupper(), s)) and
            any(map(lambda c: c.islower(), s)) and
            any(map(lambda c: c.isdigit(), s)) and
            len(s) >= 8)
print(check_string("Python123"))
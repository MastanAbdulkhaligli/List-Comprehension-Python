"""
Mastan Abdulkhaligli 
List Comprehension Exercises
6-10
"""

# 6. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

upper_fruits = [i.upper() for i in fruits  ]
print(upper_fruits)



# 7.  Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

odd_negative_numbers = [i for i in numbers if (i<0 ) and (i%2!=0) ]
print(odd_negative_numbers)







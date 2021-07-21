"""
Mastan Abdulkhaligli 
List Comprehension Exercises
1-5
"""


# 1. Find all of the numbers from 1–1000 that are divisible by 8

div_by_8 = [i for i in range(1,1000) if i%8 == 0] 
print(div_by_8)
print("*"*150)

# 2. Find all of the numbers from 1–1000 that have a 6 in them
six_in_them = [i for i in range(1,1000) if "6" in str(i)]
print(six_in_them)
print("*"*150)

# 3. Count the number of spaces in a string (use string below)
string = "Practice Problems to Drill List Comprehension in Your Head."

number_of_spaces = len([i for i in string if i== " "])
print(number_of_spaces)
print("*"*150)



# 4. Remove all of the vowels in a string (use string above)
without_vowels = [i for i in string if i not in ["a", "e", "i", "o", "u", "y"] ]
print(without_vowels)
print("*"*150)



# 5. Find all of the words in a string that are less than 5 letters (use string above)

less_than_five = [i for i in string.split() if len(i) <5]
print(less_than_five)
print("*"*150)


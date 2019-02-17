# Python_Workshop.Jan19

This repo contains the codes of second intro class and the assignments related to them:

Assignments:-

# Conditional statement and Loop

1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).

2. Create a for loop that prompts the user for a hobby 3 times, then appends each one to
hobbies.

3. We add a Leap Day on February 29, almost every four years. The leap day is an extra, or
intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800,
1900, 2100, 2200, 2300 and 2500 are NOT leap years.

4. Write a Python program to count the number of even and odd numbers from a series of
numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

5. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5

6. Write a Python program which takes two digits m (row) and n (column) as input and
generates a two-dimensional array. The element value in the i-th row and j-th column of the
array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

7. Write a Python program to check the validity of password input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].

At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

8. Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each
dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73

9. Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999



# Functions
1. Write a Python function to find the Max of three numbers.

2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20

3. Write a Python function to calculate the factorial of a number (a non-negative integer). The
function accepts the number as an argument.

4. Define a function is_even that will take a number x as input.If x is even, then return True.
Otherwise, return False.

5. Write a function called digit_sum that can take any mumber of intiger argiments takes returns
the sum of all that number's digits.

6. Write a Python function that accepts a string and calculate the number of upper case letters
and lower case letters.
Sample String : 'The quick Brow Fox'

Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

7. Write a shutting down program:
First, def a function, shut_down, that takes one argument s. Then, if the shut_down function
receives an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no",
then the function should return "Shutdown aborted". Finally, if shut_down gets anything other
than those inputs, the function should return "Sorry".



# String
1. Write a Python program to calculate the length of a string. Do not use built-in len() function.

2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

3. Write a Python program to get a string from a given string where all occurrences of its first
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'



# List
1. Write a Python program to sum all the items in a list. Do not use built-in sum() function.

2. Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

3. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

4. Write a Python program to create a list by concatenating a given list which range goes from 1
to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

5. Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000",
"#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red',
'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name':
'Yellow', 'color_code': '#FFFF00'}]

6. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

7. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

8. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]




# Dictionary
1. Write a Python script to sort (ascending and descending) a dictionary by value.

2. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

3. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

4. Write a Python script to check if a given key already exists in a dictionary.

5. Write a Python program to iterate over dictionaries using for loops.

6. Write a Python script to generate and print a dictionary that contains a number (between 1
and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

7. Write a Python script to merge two Python dictionaries.

8. Write a Python program to sum all the items in a dictionary.

9. Write a Python program to multiply all the items in a dictionary.

10. Write a Python program to remove a key from a dictionary.

11. Write a Python program to sort a dictionary by key.

12. Write a Python program to get the maximum and minimum value in a dictionary.

13. Write a Python program to remove duplicates from Dictionary.

14. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

15. Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}



# Tuple
1. Write a Python program to add an item in a tuple.

2. Write a Python program to get the 4th element and 4th element from last of a tuple.

3. Write a Python program to check whether an element exists within a tuple.

4. Write a Python program to convert a list to a tuple.

5. Write a Python program to remove an item from a tuple.

6. Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)

7. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

8. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


# Sets
1. Write a Python program to create a set and demonstrate 7 methods that can be done with set
datastructure.

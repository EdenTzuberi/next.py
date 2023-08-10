import functools


def combine_coins(coin, numbers):
    """
    This function adds coin sign next to the numbers.
    for example: if coin = '$' and numbers = range (0, 4) the function will return $0, $1, $2, $3
    :param coin: coin sign
    :param numbers: numbers range
    :return: coin sign + number
    :rtype: str
    """
    coins = [coin + str(num) for num in numbers]
    return ', '.join(coins)


print(combine_coins('$', range(4)))
print('\n')


####################################################################################################

# map function example:

def square(num):
    """
    :param num: a number to square
    :return: squared number
    :rtype: int
    """
    return num ** 2


list_of_numbers = [2, 3, 4, 5, 6]
result = map(square, list_of_numbers)
print(list(result))
print('\n')


####################################################################################################


# 1.1.2
def double_char(char):
    """
    :param char: letter char
    :return: doubled char
    :rtype: str
    """
    return char * 2


def double_letter(my_str):
    """
    :param my_str: string
    :return: a new string with each letter doubled
    :rtype: str
    """
    return ''.join(list(map(double_char, my_str)))


print(double_letter("python"))
print(double_letter("we are the champions!"))
print('\n')


####################################################################################################


# 1.1.3

def four_div(num):
    """
    :param num: number, type int
    :return: True, if the number divided by 4 without a remainder
    :rtype: bool
    """
    return num % 4 == 0


def four_dividers(number):
    """
    :param number: max number
    :return: a list with all the numbers from 1 to the max number that's divided by 4 without a reminder.
    :rtype: list
    """
    return list(filter(four_div, range(1, number + 1)))


print(four_dividers(9))
print(four_dividers(3))
print('\n')


####################################################################################################

def add(a, b):
    """
    :param a: num1
    :param b: num2
    :return: the addition between to numbers
    :rtype: int
    """
    return int(a) + int(b)


def sum_of_digits(number):
    """
    :param number: number
    :return: a new number, the sum of the digits of the number.
    :rtype: int
    """
    return functools.reduce(add, list(str(number)))


print(sum_of_digits(104))
print(sum_of_digits(2019))
print('\n')
####################################################################################################
# lambda function

print((lambda x, y: x + y)(1, 6))
print('\n')

a = lambda x: 1
print(a(3))
print(a("s"))
print(a(2))
print(type(a(3)))
print('\n')

b = lambda x: x
print(b(1))
print(b(3))
print('\n')

c = lambda x, y: x + y
print(c(1, 3))
print(c(2, 5))
print('\n')

d = lambda x, y: y
print(d(1, 3))
print(d(5, 2))
print('\n')


# 1.2.5

def function(num, item):
    return num + 1


# password = input("Enter Your password (integers only): ")
# password = '1234'
# lst = list(map(int, password))
# print(lst)
# magic = functools.reduce(function, lst)
# print(magic)
# result = (lambda x: x % 4 == 0)(magic)
# print(result)
#
# if result:
#     print("Correct password!")
# else:
#      print("Wrong password.")


####################################################################################################


# 1.3.1
def intersection(list_1, list_2):
    """
    The function takes two lists as input and returns a new list that is a result of slicing elements from both input
    lists.
    :param list_1: list1
    :param list_2: list2
    :return: list with slicing elements
    :rtype: list
    """
    # return list(dict.fromkeys([x for x in list_1 if x in list_2]))      # another solution
    return list(set([x for x in list_1 if x in list_2]))


print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
print('\n')


####################################################################################################

# 1.3.2
def is_prime(number):
    """
    The function takes a number and returns a Boolean value indicating whether it is prime (True for prime,
    False for non-prime). A prime number is a number that is divisible only by itself and 1, without any remainder.
    :param number: int number
    :return: True or False
    :rtype: bool
    """
    return all(number % x != 0 for x in range(2, number))
    # all() function to check if the number is not divisible by any element in the range from 2 to number - 1.


print(is_prime(42))
print(is_prime(43))
print('\n')


####################################################################################################


# 1.3.3 - rewrite the function "is funny()" to one line code.

# def is_funny(string):
#     for char in string:
#         if char != 'h' and char != 'a':
#             return False
#     return True

def is_funny(string):
    """
    The function returns True if all the letters in the string includes only 'a' and 'h', else False.
    :param string: string to check.
    :return: True or False.
    :rtype: bool
    """
    return set(string) == {'a', 'h'}


print(is_funny("hahahahahaha"))
print(is_funny("habhgahyahahabha"))
print('\n')

####################################################################################################


# 1.3.4

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(password)
# k -> m
# o -> q
# e -> g

new_password = []

for char in password:
    new_password.append(chr(ord(char) + 2))

print(''.join(new_password))
print('\n')
####################################################################################################


# 1.5

with open(r"C:\Users\Eden Tzuberi\Desktop\NextPy\unit1\names.txt", "r") as names_file:
    words_list = names_file.read().split()
    words_len = list(map(len, words_list))

print(words_list)
print('\n')

print(words_len)
print('\n')
# 1 - print the longest name in the list
print(max(words_list, key=len) + '\n')
print('\n')

# 2 - print the sum length of all the words in the list
print(sum(words_len))
print('\n')

# 3 - print all the short names in the list
shortest_length = len(min(words_list, key=len))
print(''.join([name + '\n' for name in words_list if len(name) == shortest_length]))
print('\n')

# 4 - create new file of names length.
with open(r"C:\Users\Eden Tzuberi\Desktop\NextPy\unit1\name_length.txt", "w") as name_length_file:
    for length in list(words_len):
        name_length_file.write(str(length) + '\n')

# 5 - Ask for number from user input, and print from names.txt all the names with the same length to this number.
length_by_user = input("Enter length names: ")
print(''.join([name + '\n' for name in words_list if len(name) == int(length_by_user)]))

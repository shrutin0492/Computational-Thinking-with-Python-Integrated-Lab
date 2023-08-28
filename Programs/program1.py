# 1. 
# a. This program prompts the user to input an integer, reverses it, and calculates the sum of the reversed integer.

# b. It checks if a given number is a factor of 255.

# c. Similar to part b, this section checks if a number is a factor of 255.

# d. Calculates the sum of two series: i. 1 + 1/3 + 1/5 + 1/7 + ... up to 'N' terms; ii. 1 + x/1! + x^3/2! + x^5/3! + x^7/4! + ... x^(2n-1)/n!

import math

# Task a
def reverse_integer_and_sum():
    num = int(input("Enter an integer: "))
    reversed_num = int(str(num)[::-1])
    sum_reversed = num + reversed_num
    print(f"Reversed: {reversed_num}")
    print(f"Sum: {sum_reversed}")

reverse_integer_and_sum()

# Task b
def is_factor(num, factor):
    return factor != 0 and num % factor == 0

num1 = int(input("Enter a number: "))
if is_factor(255, num1):
    print(f"{num1} is a factor of 255")
else:
    print(f"{num1} is not a factor of 255")

# Task c
num2 = int(input("Enter another number: "))
if is_factor(255, num2):
    print(f"{num2} is a factor of 255")
else:
    print(f"{num2} is not a factor of 255")

# Task d i
def sum_series_term(n):
    return 1 / (2 * n - 1)

N = int(input("Enter the value of N: "))
series_sum = sum(sum_series_term(i) for i in range(1, N + 1))
print(f"Sum of the series: {series_sum}")

# Task d ii
def sum_series_term_2(x, n):
    return (x ** (2 * n - 1)) / math.factorial(n - 1)

x_value = float(input("Enter the value of x: "))
N_value = int(input("Enter the value of N: "))
series_sum_2 = sum(sum_series_term_2(x_value, i) for i in range(1, N_value + 1))
print(f"Sum of the series: {series_sum_2}")
# 2.
# a. Demonstrates the built-in functions of strings, lists, and sets.

# b. Counts the occurrences of the letter 'o' in a given string.

# c. Calculates the frequency of each word in a list of strings.

# d. Stores and displays details of 'n' countries using dictionaries, including name, capital, and per capita income. Also, finds the country with the highest and second lowest per capita income.


# Task a
# Strings
string_example = "Hello, this is a string example."
print("String length:", len(string_example))
print("Uppercase:", string_example.upper())
print("Lowercase:", string_example.lower())
print("Split:", string_example.split())

# Lists
list_example = [1, 2, 3, 4, 5]
print("List length:", len(list_example))
print("Sum:", sum(list_example))
print("Sorted:", sorted(list_example))
print("List with repetition:", list_example * 3)

# Sets
set_example = {1, 2, 3, 4, 5}
print("Set length:", len(set_example))
print("Union:", set_example.union({4, 5, 6}))
print("Intersection:", set_example.intersection({3, 4, 5}))
print("Is subset:", set_example.issubset({1, 2, 3, 4, 5, 6}))

# Task b
def count_letter_o(input_string):
    return input_string.lower().count('o')

user_input = input("Enter a string: ")
o_count = count_letter_o(user_input)
print(f"Number of 'o's in the string: {o_count}")

# Task c
def word_frequency(input_string):
    words = input_string.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

user_input = input("Enter a string: ")
word_freq = word_frequency(user_input)
print("Word frequency:", word_freq)

# Task d
n = int(input("Enter the number of countries: "))
country_details = []

for _ in range(n):
    country_name = input("Enter country name: ")
    capital = input("Enter capital: ")
    per_capita_income = float(input("Enter per capita income: "))
    country_details.append({
        'country_name': country_name,
        'capital': capital,
        'per_capita_income': per_capita_income
    })

highest_income_country = max(country_details, key=lambda x: x['per_capita_income'])
second_lowest_income_country = min(sorted(country_details, key=lambda x: x['per_capita_income'])[1:], key=lambda x: x['per_capita_income'])

print("Details of the country with highest per capita income:")
print("Country:", highest_income_country['country_name'])
print("Capital:", highest_income_country['capital'])
print("Per Capita Income:", highest_income_country['per_capita_income'])

print("Details of the country with second lowest per capita income:")
print("Country:", second_lowest_income_country['country_name'])
print("Capital:", second_lowest_income_country['capital'])
print("Per Capita Income:", second_lowest_income_country['per_capita_income'])
c
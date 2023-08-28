# Computational-Thinking-with-Python-Integrated-Lab
This repository containts a collection of Python programs completed as part of Computational Thinking with Python integrated lab course in the 2nd year of my undergrad.

## Link to the colab notebook
[Colab Notebook](ctpy_integrated_lab.ipynb)

## Programs List

### Program 1: Evaluating Values, Expressions, and Statements

File: [program1.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program1.py)

Description:

a. This program prompts the user to input an integer, reverses it, and calculates the sum of the reversed integer.

b. It checks if a given number is a factor of 255.

c. Similar to part b, this section checks if a number is a factor of 255.

d. Calculates the sum of two series: i. 1 + 1/3 + 1/5 + 1/7 + ... up to 'N' terms; ii. 1 + x/1! + x^3/2! + x^5/3! + x^7/4! + ... x^(2n-1)/n!

### Program 2: Evaluating Python Collections

File: [program2.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program2.py)

Description:

a. Demonstrates the built-in functions of strings, lists, and sets.

b. Counts the occurrences of the letter 'o' in a given string.

c. Calculates the frequency of each word in a list of strings.

d. Stores and displays details of 'n' countries using dictionaries, including name, capital, and per capita income. Also, finds the country with the highest and second lowest per capita income.

### Program 3: Creating Python and Java Classes

File: [program3.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program3.py)

Description:

Defines two classes, "Python" and "Java," with data members "Version" and "name," and a method "display()" to print appropriate messages using object instances.

### Program 4: Creating Employee Class

File: [program4.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program4.py)

Description:

Defines a class "Employee" with an `__init__` method to initialize attributes like Name, Designation, and Ph. No. Also, includes a `display()` method to display employee details using instances.

### Program 5: Interactive Calculator

User input is assumed to be a formula that consist of a number, an operator
(at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.

b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError

c. If the second input is not '+' or '-', again raise a FormulaError

d. If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

File: [program5.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program5.py)

Description:

An interactive calculator that takes user input in the form of a formula (e.g., 1 + 1), validates it, performs calculations, and prints results. It raises custom exceptions for invalid inputs.

### Program 6: Counting Lines and Longest Word in a Text File

File: [program6.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program6.py)

Description:

Reads a text file, counts the number of lines, and stores each line in a list. Additionally, it identifies the longest word in the file.

### Program 7: Creating Student Details List and Writing to File

File: [program7.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program7.py)

Description:

Creates a list of student details using dictionaries, including USN, name, DOB, and email. The program then writes this list to a file.

### Program 8: Generating One-Hot Encodings using NumPy

File: [program8.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program8.py)

Description:

Generates one-hot encodings for an array using NumPy, where each unique value in the array corresponds to a binary encoded vector.

### Program 9: Importing Excel Data using Pandas

File: [program9.py](https://github.com/shrutin567/Computational-Thinking-with-Python-Integrated-Lab/blob/main/program9.py)

Description:

Imports Excel data into a Pandas DataFrame and filters the list of employees based on hire_date falling between specific months and years.

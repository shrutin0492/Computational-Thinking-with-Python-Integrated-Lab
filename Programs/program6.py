# 6.
# Reads a text file, counts the number of lines, and stores each line in a list. Additionally, it identifies the longest word in the file.

def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

def read_file_and_store(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def find_longest_word(lines):
    longest_word = ''
    for line in lines:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word

file_path = 'sample.txt'

line_count = count_lines(file_path)
print(f"Number of lines in the file: {line_count}")

lines_list = read_file_and_store(file_path)
print("Contents of the file stored in a list:")
for line in lines_list:
    print(line)

longest_word = find_longest_word(lines_list)
print(f"Longest word in the file: {longest_word}")

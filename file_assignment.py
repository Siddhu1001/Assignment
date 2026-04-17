# File Handling Assignment

# 1. Write a Python program to read an entire text file.
def read_entire_file():
    with open("sample.txt", "r") as f:
        print(f.read())

# 2. Write a Python program to read first n lines of a file.
def read_first_n_lines():
    n = 3
    with open("sample.txt", "r") as f:
        for i in range(n):
            print(f.readline(), end="")

# 3. Write a Python program to append text to a file and display the text.
def append_and_display_file():
    with open("sample.txt", "a") as f:
        f.write("\nNew text added")
    with open("sample.txt", "r") as f:
        print(f.read())

# 4. Write a Python program to read last n lines of a file.
def read_last_n_lines():
    n = 3
    with open("sample.txt", "r") as f:
        lines = f.readlines()
        print("".join(lines[-n:]))

# 5. Write a Python program to read a file line by line and store it into a list.
def file_lines_to_list():
    with open("sample.txt", "r") as f:
        lines = f.readlines()
    print(lines)

# 6. Write a Python program to read a file line by line store it into a variable.
def file_content_to_variable():
    with open("sample.txt", "r") as f:
        data = f.read()
    print(data)

# 7. Write a python program to find the longest words.
def find_longest_word():
    with open("sample.txt", "r") as f:
        words = f.read().split()
    print(max(words, key=len))

# 8. Write a Python program to count the number of lines in a text file.
def count_lines_in_file():
    with open("sample.txt", "r") as f:
        print(len(f.readlines()))

# 9. Write a Python program to count the frequency of words in a file.
def word_frequency_in_file():
    with open("sample.txt", "r") as f:
        words = f.read().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print(freq)

# 10. Write a Python program to get the file size of a plain file.
import os
def get_file_size():
    print(os.path.getsize("sample.txt"))

# 11. Write a Python program to write a list to a file.
def write_list_to_file():
    data = ["Python", "Java", "C++"]
    with open("sample.txt", "w") as f:
        for item in data:
            f.write(item + "\n")

# 12. Write a Python program to copy the contents of a file to another file .
def copy_file_content():
    with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
        f2.write(f1.read())

# 13. Write a Python program to read a random line from a file.
import random
def read_random_line():
    with open("sample.txt", "r") as f:
        lines = f.readlines()
    print(random.choice(lines))

# 14. Write a Python program to assess if a file is closed or not.
def check_file_closed():
    f = open("sample.txt", "r")
    print(f.closed)
    f.close()
    print(f.closed)

# 15.Write a Python program that takes a text file as input and returns the number of words of a given text file.
def count_words_in_file():
    with open("sample.txt", "r") as f:
        words = f.read().split()
    print(len(words))

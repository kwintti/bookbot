book = "books/frankenstein.txt"
with open(book, "r") as file:
    file_content = file.read()

def count_words(file):
    words = file.split()
    counter = 0
    for i in words:
        counter += 1
    return counter

def count_letters(file):
    letters = {}
    for chr in file:
        chr = chr.lower()
        if chr not in letters and chr.isalpha():
            letters[chr] = 1
        elif chr.isalpha():
            letters[chr] += 1
    return dict(sorted(letters.items()))

def report(words, letters, name):
    print(f"--- Begin report of {name} ---")
    print(f"{words} words found in the document.")
    for i, l in letters.items():
        print(f"The '{i}' character was found {l} times")
    print("--- End of report ---")

words = count_words(file_content)
letters = count_letters(file_content)
report(words, letters, book)


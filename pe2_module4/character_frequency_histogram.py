from os import strerror

file_name = input("Enter the desired file name: ")
try:
    stream = open(file_name, 'rt', encoding='UTF-8')
    char = stream.read(1).lower()
    char_freq = {}
    while char != '':
        if char in char_freq.keys():
            char_freq[char] += 1
        elif char.isalpha():
            char_freq[char] = 1
        char = stream.read(1).lower()
    stream.close()
    for i in sorted(char_freq):
        print(f"{i} -> {char_freq[i]}")
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

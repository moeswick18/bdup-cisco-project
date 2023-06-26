from os import strerror, path

file_name = input("Enter the desired file name: ")
try:
    read_stream = open(file_name, 'rt', encoding='UTF-8')
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

histogram_file = f"{path.splitext(file_name)[0]}.hist"
try:
    write_stream = open(histogram_file, 'wt', encoding='UTF-8')
except IOError as e:
    read_stream.close()
    print(strerror(e.errno))
    exit(e.errno)

try:
    char = read_stream.read(1).lower()
    char_freq = {}
    while char != '':
        if char in char_freq.keys():
            char_freq[char] += 1
        elif char.isalpha():
            char_freq[char] = 1
        char = read_stream.read(1).lower()
    read_stream.close()
    for i, j in sorted(char_freq.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
        write_stream.write(f"{i} -> {j}\n")
        print(f"{i} -> {j}")
    write_stream.close()
except IOError as e:
    read_stream.close()
    write_stream.close()
    print(strerror(e.errno))
    exit(e.errno)

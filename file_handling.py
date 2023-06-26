'''import errno
import os

try:
    s = open("file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error is:", os.strerror(exc.errno))'''

'''import os

try:
    # count = 0
    char_count = line_count = 0
    stream = open("sherlock.txt", "rt", encoding="utf-8")
    # char = stream.read(1)       # read the first character
    # line = stream.readline()      # read one line
    lines = stream.readlines(20)  # without argument, returns all file contents one element per file line
    # while char !=  '':
    # while line != '':
    while(len(lines)) != 0:
        for line in lines:
            line_count += 1
            for char in line:
                print(char, end='')
                char_count += 1
        lines = stream.readlines(10)
        # line_count += 1
        # for char in line:
        #    print(char, end='')
        #    char_count += 1
        # line = stream.readline()
        # print(char, end='')
        # count += 1
        # char = stream.read(1)   # read 1 charactr
    stream.close()
    print("\n\nCharacters in file:", char_count)
    print("Lines in file:", line_count)
except IOError as e:
    print("I/O error occurred:", os.strerror(e.errno))
# print(stream.read()) # .read() read the whole file. printing the content of the file'''

'''from os import strerror

try:
    char_count = line_count = 0
    for line in open('sherlock.txt', 'rt', encoding='utf-8'):
        line_count += 1
        for char in line:
            print(char, end='')
            char_count += 1
    print("\n\nCharacters in file:", char_count)
    print("Lines in file:", line_count)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))'''

'''from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
from os import strerror

data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    # bf.readinto(data)           # for reading the binary file
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))'''

from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        print(written)
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()

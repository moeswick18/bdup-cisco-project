from os import strerror, stat

class StudentsDataException(Exception):
    """Base class for Students Data Exception"""
    pass


class BadLine(StudentsDataException):
    """Exception raised because the data inside inputted file is invalid.

    Attributes:
        file_name -- input file name which caused the error
        message -- explanation of the error
    """

    def __init__(self, file_name, message="The data inside inputted file is invalid. Correct format (without parentheses): (first_name last_name score_in_number)"):
        self.file_name = file_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_name} -> {self.message}'


class FileEmpty(StudentsDataException):
    """Exception raised because the inputted file is empty.

    Attributes:
        file_name -- input file name which caused the error
        message -- explanation of the error
    """

    def __init__(self, file_name, message="The inputted file is empty. Insert non-empty file."):
        self.file_name = file_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_name} -> {self.message}'


file_name = input("Enter Prof. Jekyll's file name: ")
try:
    stream = open(file_name, 'rt', encoding='UTF-8')
except IOError as e:
    print(strerror(e.errno))
    exit(e.errno)

try:
    if stat(file_name).st_size > 0:
        lines = stream.readlines(3)
        student_scores = {}
        while len(lines) != 0:
            for line in lines:
                processed_text = line.split()
                if len(processed_text) != 3 or (not processed_text[0].isalpha()) or (not processed_text[1].isalpha()):
                    raise BadLine(file_name)
                else:
                    try:
                        if f"{processed_text[0]} {processed_text[1]}" not in student_scores:
                            student_scores[f"{processed_text[0]} {processed_text[1]}"] = float(processed_text[2])
                        elif f"{processed_text[0]} {processed_text[1]}" in student_scores:
                            student_scores[f"{processed_text[0]} {processed_text[1]}"] += float(processed_text[2])
                    except ValueError:
                        raise BadLine(file_name)
            lines = stream.readlines(3)
        for i in sorted(student_scores):
            print(f"{i}\t{student_scores[i]}")
        stream.close()
    else:
        raise FileEmpty(file_name)
except FileEmpty:
    print("The inputted file is empty. Insert non-empty file.")
    stream.close()
except BadLine:
    print("The data inside inputted file is invalid. Correct format (without parentheses): (first_name last_name score_in_number)")
    stream.close()

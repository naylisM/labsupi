import json
import sys
import os

class Student():
    def __init__(self, st_number, name, birthdate, st_book):
        self.st_number, self.name, self.birthdate, self.st_book = st_number, name, birthdate, list()
        for object in st_book:
            self.st_book.append(Student_mark(**object))

class Student_mark():
    def __init__(self, subject, mark, exam_date, teacher_name):
        self.subject, self.mark, self.exam_date, self.teacher_name = subject, mark, exam_date, teacher_name

def load_data(data_folder_path):
    student_list = list()
    if os.path.isdir(data_folder_path):
        for student_json in os.listdir(data_folder_path):
            if student_json.split('.')[-1] == "json":
                file = open(os.path.join(data_folder_path,student_json), encoding='utf8')
                student_json_data = json.load(file)
                file.close()
                student_list.append(Student(**student_json_data))
    else:
        print("The specified path is not a directory or it has not been specified!\nMake sure that the path to the directory with student data is set as a parameter correctly.")
        exit()
    return student_list

if __name__ == "__main__":
    student_json_folder_path = sys.argv[-1]
    students = load_data(student_json_folder_path)
    youngest_student = max(students, key=lambda student: student.birthdate)
    oldest_student = min(students, key=lambda student: student.birthdate)
    print(f"The youngest student: {youngest_student.name} ({youngest_student.birthdate})\nThe oldest student: {oldest_student.name} ({oldest_student.birthdate})")
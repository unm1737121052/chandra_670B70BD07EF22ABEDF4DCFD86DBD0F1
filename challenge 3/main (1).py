class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of Students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students

# Example usage:
students = [
    Student("Hari", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Saumya", "A125", 9.1),
    Student("Manidhar", "A126", 9.9)
]

sorted_students = sort_students(students)

# print the sorted list of students
for Student in sorted_students:
  print(" name: {},Roll Number: {},CGPA: {}".format(Student.name,
                                                    Student.roll_number,
                                                    Student.cgpa))

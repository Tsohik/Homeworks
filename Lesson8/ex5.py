#Write a Python program to iterate over dictionaries using for loops and print out keys and values with f_string

student_grades = {
    'Ani': 18,
    'Rob': 7,
    'Anna': 15,
    'David': 8,
    'Emma': 10
}
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

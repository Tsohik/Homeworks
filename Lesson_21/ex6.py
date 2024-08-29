#Create a tuple of student names and their corresponding scores. Write a function to find the student with the highest score.

def find_highest_score(students_scores):
    top_student = students_scores[0]

    for student in students_scores[1:]:
        if student[1] > top_student[1]:
            top_student = student

    return top_student

students_scores = (
    ("Ani", 50),
    ("Simon", 98),
    ("Gor", 43),
    ("David", 88)
)

top_student = find_highest_score(students_scores)
print("Student with the highest score:", top_student)

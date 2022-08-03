student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}  # создаем новый словарь

for student in student_scores:  # для каждого студента (это его имя, key, ,будет учитываться теперь в новом списке)
    score = student_scores[
        student]  # оценка (value) будет равна оценке (value) из первого словаря для [student] каждого студента
    if score < 70:
        student_grades[student] = "Fail"  # устанавливаем (value) для нового списка согласно условий задачи
    elif score > 70:
        student_grades[student] = "Acceptable"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 90:
        student_grades[student] = "Outstanding"

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


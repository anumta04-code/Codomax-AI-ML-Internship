# Python Functions 

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


student_marks = [80, 75, 90, 85]

average = calculate_average(student_marks)

print("Student Marks:", student_marks)
print("Average Marks:", average)

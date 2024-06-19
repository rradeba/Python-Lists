#Task 1 

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()  
print(grades)

#Task 2 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

number_grades = len(grades) 
# sum function found on W3 
grades_sum = sum(grades)
average_grade = grades_sum / number_grades

print(average_grade)

#Task 3 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort() 

grades[0:2] = ("Failed", "Failed","Failed")
print(grades)
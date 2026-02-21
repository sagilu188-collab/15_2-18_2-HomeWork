#
# For each question: What is the missing operation (?)
# Solve:


# {1, 2} ? {3, 4} = {1, 2, 3, 4}

task1 = {1 , 2} | {3 , 4}
print("Task 1:")
print(task1)


# {1, 2, 3} ? {3, 4} = {3}
task2 = {1, 2, 3} & {3, 4}
print("Task 2:")
print(task2)

# {1, 2, 3, 4} ? {3, 4} = {1, 2}
task3 = {1, 2, 3, 4} - {3, 4}
print("Task 3:")
print(task3)

# {1, 2, 3} ? {3, 4} = {1, 2, 4}
task4 = {1, 2, 3} ^ {3, 4}
print("Task 4:")
print(task4)
# {1, 2, 3, 4} ? {1, 2} = True
task5 = {1, 2, 3, 4} > {1, 2}
print("Task 5:")
print(task5)

# {1, 2} ? {1, 2, 3, 4} = True
task6 = {1, 2} < {1, 2, 3, 4}
print("Task 6:")
print(task6)

# {5, 6} ? {6, 7} = {5, 6, 7}
task7 = {5, 6} | {6, 7}
print("Task 7:")
print(task7)

# {10, 11, 12} ? {12, 13} = {10, 11}
task8 = {10, 11, 12} - {12, 13}
print("Task 8:")
print(task8)


# | : איחוד (הכל ביחד)
#
# & : חיתוך (רק המשותף)
#
# - : הפרש (להוריד מהראשונה את השנייה)
#
# ^ : השונה (כל מה שלא משותף)
#
# >  < : בדיקת הכלה (מי נמצא בתוך מי)
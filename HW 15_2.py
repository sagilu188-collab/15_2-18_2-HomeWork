grades = [85, 90, 78, 92, 88]
backup_grades = grades.copy()
MoedB = [100 ,95]

grades.clear()

backup_grades.extend(MoedB)
backup_grades += [100,95]

print(backup_grades)
print(grades)




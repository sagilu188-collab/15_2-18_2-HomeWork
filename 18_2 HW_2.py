# For each question: What are the two missing operations (? ?)
#
# Example:
#
# {1, 2} ? {3, 4} ? {2} = {1, 3, 4}
#
# Answer: |  - , because-
#
# {1, 2} | {3, 4} - {2} = {1, 3, 4}
#
# You can also add brackets
# Example:
#
# {1 2 3} ? {3 4} ? { 2 } = { 2 }
#
# Answer:
#
# ( {1 2 3} - {3 4} ) & { 2 } = { 2 }
#
# Solve:
#
# {1, 2} ? {3, 4} ? {2} = {1, 3, 4}
task1 = ({1, 2} | {3, 4}) - {2}
print("Task 1:")
print(task1)

# {1, 2, 3, 4} ? {3, 4} ? {1, 2} = {1, 2, 3, 4}
task2 = {1, 2, 3, 4} & {3, 4} | {1, 2}
print("Task 2:")
print(task2)

# {1, 2, 3} ? {2, 3} ? {1, 4} = {2, 3, 4}
task3 = ({1, 2, 3} | {2, 3}) ^ {1, 4}
print("Task 3:")
print(task3)


# {1, 2, 3, 4, 5} ? {2, 4} ? {1, 2, 3} = {4, 5}
task4 = ({1, 2, 3, 4, 5} | {2, 4}) - {1, 2, 3}
print("Task 4:")
print(task4)

# {1, 2, 3, 4} ? {2, 4, 6} ? {2} = {2}
task5 = {1, 2, 3, 4} & {2, 4, 6} & {2}
print("Task 5:")
print(task5)

# {1, 2, 3, 4} ? {3, 4, 5} ? {1, 5} = {2, 3, 4}
task6 = ({1, 2, 3, 4} | {3, 4, 5}) - {1, 5}
print("Task 6:")
print(task6)

# {1, 2, 3} ? {3, 4, 5} ? {1, 2, 4} = {4, 5} ETGAR
task7 = {1, 2, 3} ^ ({3, 4, 5} | {1, 2, 4})
print("Task 7:")
print(task7)
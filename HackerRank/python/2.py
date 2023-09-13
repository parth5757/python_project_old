# this program get second last value in nested list from name and score
# url = https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# if __name__ == '__main__':
#     n = int(input("Enter the number of students: "))  # Input the number of students
    
#     students = []  # Create an empty list to store student data
    
#     # Input data for each student
#     for _ in range(n):
#         name = input("Enter student's name: ")
#         score = float(input("Enter student's score: "))
#         students.append([name, score])  # Append student data as a nested list
    
#     # Sort the students by their scores in ascending order
#     students.sort(key=lambda x: x[1])
    
#     # Find the second-lowest score
#     second_lowest_score = None
#     for student in students:
#         if student[1] != students[0][1]:
#             second_lowest_score = student[1]
#             break
    
#     # Print the names of students with the second-lowest score
#     second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    
#     # Sort the names and print them
#     second_lowest_students.sort()
#     for name in second_lowest_students:
#         print(name)


if __name__ == '__main__':
    n = int(input(""))  # Input the number of students
    
    students = []  # Create an empty list to store student data
    
    # Input data for each student
    for _ in range(n):
        name = input("")
        score = float(input(""))
        students.append([name, score])  # Append student data as a nested list
    
    # Sort the students by their scores in ascending order
    students.sort(key=lambda x: x[1])
    
    # Find the second-lowest score
    second_lowest_score = None
    for student in students:
        if student[1] != students[0][1]:
            second_lowest_score = student[1]
            break
    
    # Print the names of students with the second-lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    
    # Sort the names and print them
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)

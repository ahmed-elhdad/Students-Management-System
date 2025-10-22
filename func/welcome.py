from mod.student import Student
import os
def welcome():
    print("""
1- Press 1 to add Student
2- Press 2 to edit student
3- Press 3 to delete student
4- Press 4 to show students
5- Press 5 to exit
""")
    enter = int(input("Enter Num: \n"))
    while enter == '' or enter == None:
        int(input("Enter Num: \n"))
    if enter==1:Student.add_student()
    if enter==2:Student.edit_student()
    if enter==3:Student.delete_student()
    if enter==4:Student.list_students()
    if enter==5:os._exit(0)
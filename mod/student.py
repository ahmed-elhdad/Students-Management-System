from uuid import uuid1
from func.check_stu_score import check_study_score
students=[]
class Student:
    def __init__(self, id, name, age, grade,score):
        self.id=id
        self.name=name
        self.age=age
        self.grade=grade
        self.score=score
    def add_student():
        print('Add Student')
        try:
            uuid_id=str(uuid1(4,3))
            id=f'STU{uuid_id[:4]}'
            name=input('Enter Student Name: \n')
            if name == '':
                print('valid student name ^^')
                return
            for stu in students:
                if stu['name'].lower()==name.lower():
                    print('exit student ^^')
                    return
            age=int(input('Enter Student Age: \n'))
            if age>27:
                print("valid student age ^^")
                return
            grade=input('Enter Student Grade: \n')
            gender=input('Enter Student Gender: \n')
            if gender != 'male':
                if gender != 'female':
                    
                    print("Valid student gender ^^")
                    return
            print("Add sutdent Score: \n")
            Arabic=int(input('Enter Arabic Score: \n'))
            Math=int(input('Enter Math Score: \n'))
            English=int(input('Enter English Score: \n'))
            sience=int(input('Enter sience Score: \n'))
            socail=int(input('Enter socail Studies Score: \n'))

            Arabic_appreciation=check_study_score(Arabic)
            Math_appreciation=check_study_score(Math)
            English_appreciation=check_study_score(English)
            sience_appreciation=check_study_score(sience)
            socail_appreciation=check_study_score(socail)
            score=[]
            from mod.score import Score
            arabic_score=Score('arabic',Arabic,Arabic_appreciation)
            score.append(arabic_score.__dict__)
            
            math_score=Score('math_score',Arabic,Math_appreciation)
            score.append(math_score.__dict__)
            
            english_score=Score('english',Arabic,English_appreciation)
            score.append(english_score.__dict__)
            
            sience_score=Score('sience',Arabic,sience_appreciation)
            score.append(sience_score.__dict__)
            
            socail_score=Score('socail',socail,socail_appreciation)
            score.append(socail_score.__dict__)

            new_student=Student(id,name,age,grade,score)
            students.append(new_student.__dict__)
            print(students)
        except ValueError:
            print("Invalid data")
    def edit_student():
        print('Add Student')
    def delete_student():
        print('Add Student')
    def list_students():
        print('Add Student')
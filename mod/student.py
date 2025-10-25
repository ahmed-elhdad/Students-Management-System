from uuid import uuid1
from mod.score import Score
from func.write_txt import write_txt
from func.conver_from_json import conver_fom_json
from func.check_stu_score import check_study_score
students=[]

class Student:
    def __init__(self, id, name, age,gender, grade,score,total_score,average,presentge_score):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade
        self.score=score
        self.total_score=total_score
        self.average=average
        self.presentge_score=presentge_score
    def add_student():
        print('Add Student')
        try:
            python_txt=conver_fom_json('data/studetnts.json')
            students=[python_txt]
            uuid_id=str(uuid1(4,3))
            id=f'STU{uuid_id[:4]}'
            name=input('Enter Student Name: \n').strip()
            if name == '':
                print('valid student name ^^')
                return
            # for stu in students:
            #     print(stu)
            #     if stu['name'].lower()==name.lower():
            #         print('exit student ^^')
            #         return
            #     print('fds')
            age=int(input('Enter Student Age: \n'))
            if age>27:
                print("valid student age ^^")
                return
            elif age == 0 :
                print("Valid age")
                return
            grade=input('Enter Student Grade: \n').strip()
            gender=input('Enter Student Gender: \n').strip()
            if gender != 'male':
                if gender != 'female':
                    print("Valid student gender ^^")
                    return
            if gender == '':
                print("valid gender")
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
            arabic_score=Score('arabic',Arabic,Arabic_appreciation)
            score.append(arabic_score.__dict__)
            
            math_score=Score('math',Arabic,Math_appreciation)
            score.append(math_score.__dict__)
            
            english_score=Score('english',Arabic,English_appreciation)
            score.append(english_score.__dict__)
            
            sience_score=Score('sience',Arabic,sience_appreciation)
            score.append(sience_score.__dict__)
            
            socail_score=Score('socail',socail,socail_appreciation)
            score.append(socail_score.__dict__)
            score_average=Score.average(Arabic,Math,English,sience,socail)
            percentage_score=Score.percentage_score(Arabic,Math,English,sience,socail)
            total_score=Score.total_score(Arabic,Math,English,sience,socail)
            new_student=Student(id,name,age,gender,grade,score,total_score,score_average,percentage_score)
            students.append(new_student.__dict__)
            write_txt('data/studetnts.json',students)
        except ValueError:
            print("Invalid data")
    def edit_student():
        python_txt=conver_fom_json('data/studetnts.json')
        students=python_txt
        name=input("Enter student name: \n")
        def rules():
            print("## Write in input you want to edit it, the input you don't want to edit that press ENTER ## \n")
        for stu in students:
            if stu['name'].lower() != name.lower():
                print("Student Not Found ^^")
                return
            rules()
            will_edit=[]
            arabic_score=int(input('Enter Arabic score: \n'))
            if arabic_score != '' or socail_score is not None:
                will_edit.append(arabic_score)
                stu['score'][0]["score"]=arabic_score
                stu['score'][0]["subject_appreciation"]=check_study_score(arabic_score)
            else:
                arabic_score=stu['score'][0]['score']
            math_score=int(input('Enter Math score: \n'))
            if math_score != '' or arabic_score is not None: 
                will_edit.append(math_score)
                stu['score'][1]["score"]=math_score
                stu['score'][1]["subject_appreciation"]=check_study_score(math_score)
            else:
                math_score=stu['score'][1]['score']
            en_score=int(input('Enter English score: \n'))
            if en_score != '' or en_score is not None:    
                will_edit.append(en_score)
                stu['score'][2]["score"]=en_score
                stu['score'][2]["subject_appreciation"]=check_study_score(en_score)
            else:
                en_score=stu['score'][2]['score']
            sience_score=int(input('Enter sience score: \n'))
            if sience_score != '' or sience_score is not None:    
                will_edit.append(sience_score)
                stu['score'][3]["score"]=sience_score
                stu['score'][3]["subject_appreciation"]=check_study_score(sience_score)
                
            else:
                sience_score=stu['score'][3]['score']
            socail_score=int(input('Enter socail studies score: \n'))
            if socail_score != '' or socail_score is not None:    
                will_edit.append(socail_score)
                stu['score'][4]["score"]=socail_score
                stu['score'][4]["subject_appreciation"]=check_study_score(socail_score)
                
            else:
                socail_score=stu['score'][4]['score']
            print(will_edit)
            # Edit total score
            stu['total_score']=Score.total_score(will_edit[0],will_edit[1],will_edit[2],will_edit[3],will_edit[4])
            # Edit average score
            stu['average']=Score.average(will_edit[0],will_edit[1],will_edit[2],will_edit[3],will_edit[4])
            # Edit average score
            stu['presentge_score']=Score.percentage_score(will_edit[0],will_edit[1],will_edit[2],will_edit[3],will_edit[4])
            write_txt('data\studetnts.json',students)
    def delete_student():
        try:
            python_txt=conver_fom_json('data/studetnts.json')
            students=python_txt
            name=input("Enter Student Name: \n").strip()
            for stu in range(len(students)):
                if len(students) == 0:
                    print("No students exits")
                    return
                if students[stu]['name'].lower() != name.lower():
                    print("Student Not Found ^^")
                    return
                del students[stu]
                print(students)
                if len(students) == 0:
                    return
                write_txt('data\studetnts.json',students)
        except Exception as e:
            raise e
    def list_students():
        python_txt=conver_fom_json('data/studetnts.json')
        students=python_txt
        for stu in students:
            for stu_num in range(len(students)):
                import prettytable
                from func.convert_to_json import convert_to_json
                students_json=convert_to_json(students)
                print(
                prettytable.from_mediawiki(students))

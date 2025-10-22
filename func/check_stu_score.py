def check_study_score(subject):
    if subject>=50:
        subject_appreciation='good'
    elif subject >=70:
        subject_appreciation='very good'
    elif subject >=90:
        subject_appreciation="excellent"
    elif subject<=50:
        subject_appreciation='failed'
    return subject_appreciation
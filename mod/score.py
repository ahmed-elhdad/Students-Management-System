class Score:
    def __init__(self, subject_name,score,subject_appreciation):
        self.subject_name=subject_name
        self.score=score
        self.subject_appreciation=subject_appreciation
    def average(arabic,math,en,sience,socail):
        total=int((arabic + math + en + sience + socail)/2)
        return total
    def total_score(arabic,math,en,sience,socail):
        total=int(arabic + math + en + sience + socail)
        return total
    def percentage_score(arabic,math,en,sience,socail):
        percentage=int((arabic + math + en + sience + socail/500)*100)
        return percentage
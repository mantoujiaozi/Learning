import os
# for的使用
print([d for d in os.listdir('.')])
L = ['Hello', 'World', 18, 'OK']
print([s.lower() for s in L if isinstance(s, str)])
print([x*x for x in range(1, 11)])
print([x*x for x in range(1, 11) if x % 2 == 0])
print([m+n for m in 'ABC' for n in 'XYZ'])


# 类的使用
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Echo', 60)
bart.print_score()
print(bart.get_grade())

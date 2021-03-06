'''
row sample record example observation

'''
from collections import namedtuple

# 번호, 이름, 수학, 과학, 컴퓨터
from typing import NamedTuple

student_1 = (1, '홍길동', 10, 20, 30)
print('번호 :', student_1[0])
print('과학 :', student_1[3])

# 튜플 (tuple) 타입의 단점
#   - 해당 인덱스의 원소가 무슨 값을 의미하는지 파악하지 어렵다.
#   - 특정 원소에 접근(read/write) 하기 위해서는 정수 인덱스만 사용해야 한다.

# 튜플의 단점을 해결하기 위해서
# 튜플의 특징과 딕셔너리(dict)의 특징을 모두 갖는 NamedTuple 클래스

Student = namedtuple('Student', ('no', 'name', 'math', 'science', 'cs'))
student_2 = Student(3, '허균', 100, 100, 100)
print(student_2)
print(f'번호: {student_2[0]}, {student_2.no}')
print(f'수학: {student_2[2]}, {student_2.math}')


# Python 3.6 부터 NamedTuple 을 class 처럼 선언하는 방식이 만들어 짐
class Student2(NamedTuple):  # Student2 클래스는 NamedTuple 클래스를 상속
    # field 선언 - 변수 타입 annotation 을 반드시 추가해야 함
    no: int
    name: str
    math: int
    science: int
    cs: int

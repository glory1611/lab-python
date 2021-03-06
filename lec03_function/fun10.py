'''
파이썬에서 함수는 1급 객체(first-class object)
    - 함수를 변수에 저장할 수 있음
    - 매개변수(paramiter)에 함수를 전달 할 수 있음
    - 함수가 다른 함수를 리턴할 수 있름
    - 함수 내부에서 다른 함수를 정의할 수 있음
'''

def twice(x):
    return 2 * x

result = twice(100) # 함수 호출 -> 함수의 리턴 값을 변수에 저장
print(result)   # 리턴 값을 출력


double = twice  # 함수를 변수에 저장
print(double)
result = double(11) # 함수 호출
print(result)


def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def calculate(x, y, operator):
    return operator(x, y)


result = calculate(1, 2, plus)
print(result)


def decorate(func):
    print('decorate 함수 내부:', func.__name__)
    def wrapper_function(*args):
        print('다음 함수를 실행:', func.__name__)
        return func(*args)
    return wrapper_function


wrapper = decorate(print)
wrapper('a', 'b', 'c')


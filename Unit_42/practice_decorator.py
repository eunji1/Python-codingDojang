def type_check(type_a, type_b):
    def real_decorator(func):
        def wrapper(a, b):
            #호출할 함수의 매개변수가 데코레이터에 지정한 자료형(클래스)의 인스턴스인지 확인
            if isinstance(a, type_a) and isinstance(b, type_b):
                return func(a, b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator

@type_check(int, int) #매개변수가 있는 데코레이터
def add(a, b):
    return a + b

print(add(10, 20))
print(add('hello', 'world'))

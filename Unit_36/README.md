# Unit 36. 클래스 상속 사용하기

## 36.3 기반 클래스의 속성 사용하기

### 36.3.1  super()로 기반 클래스 초기화하기
이때는 super()를 사용해서 기반 클래스의 ```__init__ 메서드```를 호출해준다. 
다음과 같이 ```super()``` 뒤에 ```.(점)```을 붙여서 메서드를 호출하는 방식

- super().메서드()
```
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)
```

### 36.3.2  기반 클래스를 초기화하지 않아도 되는 경우
만약 파생 클래스에서 ```__init__ 메서드```를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 된다.
```
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    pass
 
james = Student()
print(james.hello)
```

## 36.4 메서드 오버라이딩 사용하기
오버라이딩(overriding)은 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻임

오버라이딩된 메서드에서 super()로 기반 클래스의 메서드를 호출해봅니다.
```
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()
```

## 36.5 다중 상속 사용하기
```
class 기반클래스이름1:
    코드
 
class 기반클래스이름2:
    코드
 
class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
    코드
```
```
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
 
james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드
```


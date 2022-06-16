# Unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기

## 35.1 클래스 속성과 인스턴스 속성 알아보기
### 35.1.1  클래스 속성 사용하기
```
class 클래스이름:
    속성 = 값
```
```
class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)
-----------------------------------------
실행 결과
['책', '열쇠']
['책', '열쇠']
```
james와 maria 인스턴스를 만들고 각자 put_bag에 넣었는데 실행결과는 합쳐서 나옴  
즉, 클래스 속성은 클래스에 속해있으며 모든 인스턴스에서 공유함

<details>
<summary>[그림 35-1] 클래스 속성
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13898/mod_page/content/6/035001.png)

</div>
</details>

### 5.1.2  인스턴스 속성 사용하기
bag을 인스턴스 속성으로 만들면 인스턴스별로 독립되어 서로 영향을 주지 않음
```
class_instance_attribute.py
class Person:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)
----------------------------------------------------
실행 결과
['책']
['열쇠']
```
- 클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
- 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

## 35.2 정적 메서드 사용하기
인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 정적 메서드와 클래스 메서드

정적 메서드는 다음과 같이 메서드 위에 ```@staticmethod```를 붙입니다. 이때 정적 메서드는 매개변수에 self를 지정하지 않습니다.
```
class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드
```
```
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출
-------------------------------------------------------
실행 결과
30
200
```
- 클래스.메서드()
```
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출
```
## 35.3 클래스 메서드 사용하기
클래스 메서드는 다음과 같이 메서드 위에 ```@classmethod```를 붙입니다. 이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 합니다(cls는 class에서 따왔습니다).
```
class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드
```

```
class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.
-----------------------------------------------------
2명 생성되었습니다.
```


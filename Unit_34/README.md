# Unit 34. 클래스 사용하기

## 34.1 클래스와 메서드 만들기
클래스는 class에 클래스 이름을 지정하고 ```:(콜론)```을 붙인 뒤 다음 줄부터 def로 메서드를 작성하면 된다.

보통 클래스의 이름은 대문자로 시작  
특히 메서드의 첫 번째 매개변수는 반드시 self를 지정해야 합니다.
```
class 클래스이름:
    def 메서드(self):
        코드
```
다음과 같이 클래스에 ```()(괄호)```를 붙인 뒤 변수에 할당합니다.

- 인스턴스 = 클래스()
```
>>> james = Person()
```
Person으로 변수 james를 만들었는데 이 james가 Person의 인스턴스(instance)  
클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야함

## 34.1.3  인스턴스와 객체의 차이점?
사실 인스턴스와 객체는 같은 것을 뜻함  
보통 객체만 지칭할 때는 객체(object), 클래스와 연관지어서 말할 때는 인스턴스(instance) 
그래서 다음과 같이 리스트 변수 a, b가 있으면 a, b는 객체 a와 b는 list 클래스의 인스턴스
```
>>> a = list(range(10))
>>> b = list(range(20))
```
## 34.2 속성 사용하기
속성(attribute)을 만들 때는 ```__init__``` 메서드 안에서 self.속성에 값을 할당
```
class 클래스이름:
    def __init__(self):
        self.속성 = 값
```
## 34.2.1  self의 의미
self는 인스턴스 자기 자신을 의미  
여기서 __init__의 매개변수 self에 들어가는 값은 Person()   
그리고 self가 완성된 뒤 james에 할당되어, 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어오게됨


<details>
<summary>[그림 34-4] 인스턴스와 self
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13877/mod_page/content/3/034004.png)

</div>
</details>

## 34.3 비공개 속성 사용하기

```
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
```

이번에는 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있는 비공개 속성(private attribute)을 사용
```
class 클래스이름:
    def __init__(self, 매개변수)
        self.__속성 = 값
```
```
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
```
```
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
--------------------------------------------------------
실행 결과
이제 7000원 남았네요.
```




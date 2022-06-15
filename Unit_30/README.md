# Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
함수에서 위치 인수, 키워드 인수를 사용하는 방법과 리스트, 딕셔너리 언패킹(unpacking)을 활용하는 방법
## 30.1 위치 인수와 리스트 언패킹 사용하기
다음과 같이 함수에 인수를 순서대로 넣는 방식을 위치 인수(positional argument)라고 함
즉, 인수의 위치가 정해져 있음
```
>>> print(10, 20, 30)
10 20 30
```
### 30.1.1  위치 인수를 사용하는 함수를 만들고 호출하기
```
>>> def print_numbers(a, b, c):
...     print(a)
...     print(b)
...     print(c)
...
```
print_numbers에 숫자 세 개를 넣으면 각 줄에 숫자가 출력
```
>>> print_numbers(10, 20, 30)
10
20
30
```
### 30.1.2  언패킹 사용하기
이렇게 인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수도 있음  
다음과 같이 리스트 또는 튜플 앞에 ```*(애스터리스크)```를 붙여서 함수에 넣어주기

- 함수(*리스트)
- 함수(*튜플)
```
>>> x = [10, 20, 30]
>>> print_numbers(*x)
10
20
30
```
즉, 리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 되어서 print_numbers(10, 20, 30)과 똑같은 동작이 된다.

<details>
<summary>[그림 30-1] 리스트 언패킹
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13788/mod_page/content/2/030001.png)
</div>
</details>

## 30.1.3  가변 인수 함수 만들기
그럼 위치 인수와 리스트 언패킹은 어디에 사용할까요?  
이 기능들은 인수의 개수가 정해지지 않은 가변 인수(variable argument)에 사용!
즉, 같은 함수에 인수 한 개를 넣을 수도 있고, 열 개를 넣을 수도 있습니다. 또는, 인수를 넣지 않을 수도 있습니다.
```
def 함수이름(*매개변수):
    코드
```
```
>>> def print_numbers(*args):
...     for arg in args:
...         print(arg)
```
```
>>> print_numbers(10)
10
>>> print_numbers(10, 20, 30, 40)
10
20
30
40
```
```
>>> x = [10]
>>> print_numbers(*x)
10
>>> y = [10, 20, 30, 40]
>>> print_numbers(*y)
10
20
30
40
```
```
참고 | 고정 인수와 가변 인수를 함께 사용하기
고정 인수와 가변 인수를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 *를 붙여주면 됩니다.

>>> def print_numbers(a, *args):
...     print(a)
...     print(args)
...
>>> print_numbers(1)
1
()
>>> print_numbers(1, 10, 20)
1
(10, 20)
>>> print_numbers(*[10, 20, 30])
10
(20, 30)
단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.
```

## 30.3 키워드 인수와 딕셔너리 언패킹 사용하기
딕셔너리 앞에 **(애스터리스크 두 개)를 붙여서 함수에 넣어줍니다.

- 함수(**딕셔너리)
```
>>> def personal_info(name, age, address):
...     print('이름: ', name)
...     print('나이: ', age)
...     print('주소: ', address)
```
```
>>> x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
>>> personal_info(**x)
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동
```
<details>
<summary>[그림 30-2] 딕셔너리 언패킹
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13790/mod_page/content/2/030002.png)
</div>
</details>

## 30.3.2  키워드 인수를 사용하는 가변 인수 함수 만들기
다음과 같이 키워드 인수를 사용하는 가변 인수 함수는 ```매개변수 앞에 **```를 붙여서 만듭니다.
```
def 함수이름(**매개변수):
    코드
```
```
>>> def personal_info(**kwargs):
...     for kw, arg in kwargs.items():
...         print(kw, ': ', arg, sep='')
```
- 매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 keyword arguments를 줄여서 kwargs로 사용
- 특히 이 kwargs는 딕셔너리라서 for로 반복할 수 있다.
```
>>> personal_info(name='홍길동')
name: 홍길동
>>> personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
```
딕셔너리 언패킹을 사용
```
>>> x = {'name': '홍길동'}
>>> personal_info(**x)
name: 홍길동
>>> y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
>>> personal_info(**y)
name: 홍길동
age: 30
address: 서울시 용산구 이촌동
```

이처럼 함수를 만들 때 ```def personal_info(**kwargs):```와 같이 매개변수에 **를 붙여주면 키워드 인수를 사용하는 가변 인수 함수를 만들 수 있음
 
- 보통 **kwargs를 사용한 가변 인수 함수는 다음과 같이 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듦
```
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])
```
## 30.4 매개변수에 초깃값 지정하기
인수를 생략할 수는 없을까?
이때는 함수의 매개변수에 초깃값을 지정
```
def 함수이름(매개변수=값):
    코드
```
매개변수의 초깃값은 주로 사용하는 값이 있으면서 가끔 다른 값을 사용해야 할 때 활용한다. 
- 대표적인 예가 print 함수

이제 ```personal_info``` 함수에서 매개변수 address의 초깃값을 '비공개'로 지정
```
>>> def personal_info(name, age, address='비공개'):
...     print('이름: ', name)
...     print('나이: ', age)
...     print('주소: ', address)
```
address는 초깃값이 있으므로 personal_info는 다음과 같이 address 부분을 비워 두고 호출할 수 있음
```
>>> personal_info('홍길동', 30)
이름:  홍길동
나이:  30
주소:  비공개
```
매개변수에 초깃값이 지정되어 있더라도 값을 넣으면 해당 값이 전달됨
```
>>> personal_info('홍길동', 30, '서울시 용산구 이촌동')
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동
```
### 30.4.1  초깃값이 지정된 매개변수의 위치
매개변수의 초깃값을 지정할 때 한 가지 주의할 점 
초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없다.

```
def personal_info(name, age, address='비공개'):
def personal_info(name, age=0, address='비공개'):
def personal_info(name='비공개', age=0, address='비공개'):
```

# Unit 33. 클로저 사용하기

## 33.1 변수의 사용 범위 알아보기
```
x = 10          # 전역 변수
def foo():
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력
```
<details>
<summary>[그림 33-1] 전역 변수와 전역 범위
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13866/mod_page/content/3/033001.png)

</div>
</details>

```
def foo():
    x = 10      # foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()
print(x)        # 에러. foo의 지역 변수는 출력할 수 없음
```

<details>
<summary>[그림 33-2] 지역 변수와 지역 범위
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13866/mod_page/content/3/033002.png)

</div>
</details>

## 33.1.1  함수 안에서 전역 변수 변경하기
```
x = 10          # 전역 변수
def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()
print(x)        # 전역 변수 출력
--------------------------------------
실행 결과
20
10
```
- global 전역변수
```
x = 10          # 전역 변수
def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력
------------------------------------------------
20
20
```

## 33.2 함수 안에서 함수 만들기
```
def 함수이름1():
    코드
    def 함수이름2():
        코드
```
### 33.2.1  지역 변수의 범위

```
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)    # 바깥쪽 함수의 지역 변수를 사용
```
바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있음

### 33.2.2  지역 변수 변경하기

다음과 같이 안쪽 함수 B에서 바깥쪽 함수 A의 지역 변수 x를 변경해봅니다.

```
def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()
----------------------------------------
실행 결과
10
```
- nonlocal 지역변수
```
def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()
---------------------------------------------------------
실행 결과
20
```

## 33.3 클로저 사용하기
```
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))
---------------------------------------------------------
실행 결과
8 11 14 17 20
```
<details>
<summary>[그림 33-4] 클로저의 개념
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13868/mod_page/content/3/033004.png)

</div>
</details>


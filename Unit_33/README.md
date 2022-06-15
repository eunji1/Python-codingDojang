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

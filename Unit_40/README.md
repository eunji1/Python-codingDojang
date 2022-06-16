# Unit 40. 제너레이터 사용하기
**제너레이터** 는 이터레이터를 생성해주는 함수
- 이터레이터는 클래스에 ```__iter__, __next__ 또는 __getitem__ 메서드```를 구현
- 하지만 제너레이터는 함수 안에서 yield라는 키워드만 사용

## 40.1 제너레이터와 yield 알아보기
함수 안에서 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)을 지정

- yield 값
```
def number_generator():
    yield 0
    yield 1
    yield 2
 
for i in number_generator():
    print(i)
--------------------------------------
실행 결과
0
1
2
```

### 40.1.2  for와 제너레이터

<details>
<summary>[그림 40-1] for 반복문과 제너레이터
</summary>
<div markdown="1">       

😎

for 반복문은 반복할 때마다 __next__를 호출하므로 yield에서 발생시킨 값을 가져온다. 그리고 StopIteration 예외가 발생하면 반복을 끝낸다

![](https://dojang.io/pluginfile.php/13960/mod_page/content/4/040001.png)

</div>
</details>

### 40.1.3  yield의 동작 과정 알아보기
for 반복문 대신 next 함수로 ```__next__ 메서드```를 직접 호출해보겠습니다.

- 변수 = next(제너레이터객체)
```
def number_generator():
    yield 0    # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1    # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 2    # 2를 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
 
g = number_generator()
 
a = next(g)    # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)       # 0
 
b = next(g)
print(b)       # 1
 
c = next(g)
print(c)       # 2
--------------------------------------------------------------------------
실행 결과
0
1
2
```
## 40.2 제너레이터 만들기
range(횟수)처럼 동작을 하는 제너레이터 만들기
```
def number_generator(stop):
    n = 0              # 숫자는 0부터 시작
    while n < stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n        # 현재 숫자를 바깥으로 전달
        n += 1         # 현재 숫자를 증가시킴
 
for i in number_generator(3):
    print(i)
```
## 40.3 yield from으로 값을 여러 번 바깥으로 전달하기
```
def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i
 
for i in number_generator():
    print(i)
```
이런 경우에는 매번 반복문을 사용하지 않고, yield from을 사용

- yield from 반복가능한객체
- yield from 이터레이터
- yield from 제너레이터객체

```
def number_generator():
    x = [1, 2, 3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달
 
for i in number_generator():
    print(i)
```



# Unit 39. 이터레이터 사용하기
**이터레이터(iterator)** 는 값을 차례대로 꺼낼 수 있는 객체(object)
## 39.1 반복 가능한 객체 알아보기
- 우리가 흔히 사용하는 문자열, 리스트, 딕셔너리, 세트가 반복 가능한 객체
- 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체

```
>>> it = [1, 2, 3].__iter__()
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    it.__next__()
StopIteration
```
이처럼 이터레이터는 __next__로 요소를 계속 꺼내다가 꺼낼 요소가 없으면 StopIteration 예외를 발생시켜서 반복을 끝냄

## 39.1.1  for와 반복 가능한 객체

<details>
<summary>[그림 39-1] for에서 range의 동작 과정
</summary>
<div markdown="1">       

😎

for에 range(3)을 사용했다면 먼저 range에서 __iter__로 이터레이터를 얻는다.  
그리고 한 번 반복할 때마다 이터레이터에서 __next__로 숫자를 꺼내서 i에 저장하고, 지정된 숫자 3이 되면 StopIteration을 발생시켜서 반복을 끝낸다.

![](https://dojang.io/pluginfile.php/13952/mod_page/content/3/039001.png)

</div>
</details>

## 39.2 이터레이터 만들기
```
class 이터레이터이름:
    def __iter__(self):
        코드
 
    def __next__(self):
        코드
```
```
class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')
--------------------------------------------------------
실행 결과
0 1 2
```

## 39.3 인덱스로 접근할 수 있는 이터레이터 만들기
```
class 이터레이터이름:
    def __getitem__(self, 인덱스):
        코드
```
```
class Counter:
    def __init__(self, stop):
        self.stop = stop
 
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
 
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
 
for i in Counter(3):
    print(i, end=' ')
------------------------------------------------
실행 결과
0 1 2
0 1 2
```
클래스에서 ```__getitem__ 메서드```를 구현하면 인덱스로 접근할 수 있는 이터레이터가 된다.  

## 39.4 iter, next 함수 활용하기
### 39.4.1  iter
iter는 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝냄  
- iter(호출가능한객체, 반복을끝낼값)
```
>>> import random
>>> it = iter(lambda : random.randint(0, 5), 2) #0부터 5까지 무작위 숫자 생성 , 2가 나오면 반복을 끝냄
>>> next(it)
0
>>> next(it)
3
>>> next(it)
1
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    next(it)
StopIteration
```
## 39.4.2  next
next는 기본값을 지정
기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력
- next(반복가능한객체, 기본값)
```
>>> it = iter(range(3))
>>> next(it, 10)
0
>>> next(it, 10)
1
>>> next(it, 10)
2
>>> next(it, 10)
10
>>> next(it, 10)
10
```



# Unit 32. 람다 표현식 사용하기

## 32.1 람다 표현식으로 함수 만들기
```
>>> def plus_ten(x):
...     return x + 10
...
>>> plus_ten(1)
11
```
람다 표현식은 다음과 같이 lambda에 매개변수를 지정하고 :(콜론) 뒤에 반환값으로 사용할 식을 지정
- lambda 매개변수들: 식
```
>>> lambda x: x + 10
<function <lambda> at 0x02C27270>
```
## 32.1.1  람다 표현식 자체를 호출하기
다음과 같이 람다 표현식을 ```( )(괄호)```로 묶은 뒤에 다시 ```( )```를 붙이고 인수를 넣어서 호출하면 됩니다.
```
(lambda 매개변수들: 식)(인수들)
>>> (lambda x: x + 10)(1)
11
```
## 32.1.2  람다 표현식 안에서는 변수를 만들 수 없다
반환값 부분은 변수 없이 식 한 줄로 표현할 수 있어야함
```
>>> (lambda x: y = 10; x + y)(1)
SyntaxError: invalid syntax
```
## 32.2 람다 표현식과 map, filter, reduce 함수 활용하기
### 32.2.1  람다 표현식에 조건부 표현식 사용하기

- lambda 매개변수들: 식1 if 조건식 else 식2
```
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(map(lambda x: str(x) if x % 3 == 0 else x, a))
[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
```

<details>
<summary>[그림 32-2] map에 람다 표현식 사용하기
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13855/mod_page/content/3/032002.png)

</div>
</details>

## 32.2.4  reduce 사용하기
reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수  
(reduce는 파이썬 3부터 내장 함수가 아닙니다. 따라서 functools 모듈에서 reduce 함수를 가져와야 합니다)

- from functools import reduce
- reduce(함수, 반복가능한객체)
```
>>> def f(x, y):
...     return x + y
...
>>> a = [1, 2, 3, 4, 5]
>>> from functools import reduce
>>> reduce(f, a)
15
```
<details>
<summary>[그림 32-4] reduce 함수
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13855/mod_page/content/3/032004.png)

</div>
</details>

```
>>> a = [1, 2, 3, 4, 5]
>>> from functools import reduce
>>> reduce(lambda x, y: x + y, a)
15
```


# Unit 26. 세트 사용하기
## 26.1 세트 만등기
세트는 ```{ }``` 안에 값을 저장하며 각 값은 ```,```로 구분
- 세트 = {값1, 값2, 값3}

세트는 요소의 순서가 정해져있지 않음 (unordered)  
따라서 세트를 출력해보면 매번 요소의 순서가 다르게 나옴
또, 세트에 들어가는 요소는 중복 될 수 없음
```
>>> fruits = {'orange', 'orange', 'cherry'}
>>> fruits
{'cherry', 'orange'}
```
### 26.1.1 세트에 특정 값이 있는지 확인하기
in 연산자 사용
- 값 in 세트
```
>>> fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
>>> 'orange' in fruits
True
>>> 'peach' in fruits
False
```
- 값 not in 세트

### 26.1.2  set를 사용하여 세트 만들기
- set(반복가능한객체)
```
>>> a = set('apple')    # 유일한 문자만 세트로 만듦
>>> a
{'e', 'l', 'a', 'p'}
```
```
>>> b = set(range(5))
>>> b
{0, 1, 2, 3, 4}
```
빈 세트는 ```c =set()```  
단, ```c={}```와 같이 만들면 빈 딕셔너리가 만들어지므로 주의
```
>>> c = set()
>>> c
set()
```

```
참고| 프로즌 세트
프로즌세트 = frozenset(반복가능한객체)

>>> a = frozenset(range(10))
>>> a
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

frozenset는 뒤에서 설명할 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없습니다.
```
## 26.2 집합 연산 사용하기
```| 연산자```는 합집합(union)을 구하며 OR 연산자 |를 사용 
```set.union``` 메서드와 동작이 같다. 
- 세트1 | 세트2
- set.union(세트1, 세트2)
```
>>> a = {1, 2, 3, 4}
>>> b = {3, 4, 5, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}
>>> set.union(a, b)
{1, 2, 3, 4, 5, 6}
```
```& 연산자```는 교집합(intersection)을 구하며 AND 연산자 &를 사용  
```set.intersection``` 메서드와 동작이 같다.
- 세트1 & 세트2
- set.intersection(세트1, 세트2)
```
>>> a & b
{3, 4}
>>> set.intersection(a, b)
{3, 4}
```
```- 연산자```는 차집합(difference)을 구하며 뺄셈 연산자 -를 사용  
```set.difference``` 메서드와 동작이 같다.
- 세트1 - 세트2
- set.difference(세트1, 세트2)
```
>>> a - b
{1, 2}
>>> set.difference(a, b)
{1, 2}
```
```^ 연산자```는 대칭차집합(symmetric difference)을 구하며 XOR 연산자 ^를 사용  
```set.symmetric_difference``` 메서드와 동작이 같습니다.

대칭차집합은 XOR 연산자의 특성을 그대로 따르는데 XOR은 서로 다르면 참입니다.  
따라서 집합에서는 두 집합 중 겹치지 않는 요소만 포함합니다.
- 세트1 ^ 세트2
- set.symmetric_difference(세트1, 세트2)
```
>>> a ^ b
{1, 2, 5, 6}
>>> set.symmetric_difference(a, b)
{1, 2, 5, 6}
```
### 26.2.1  집합 연산 후 할당 연산자 사용하기
세트 자료형에 ```|, &, -, ^ 연산자```와 ```할당 연산자 =```을 함께 사용하면 집합 연산의 결과를 변수에 다시 저장(할당)합니다.

```|=```은 현재 세트에 다른 세트를 더하며 update 메서드와 같습니다. 
- 세트1 |= 세트2
- 세트1.update(세트2)
```
>>> a = {1, 2, 3, 4}
>>> a |= {5}
>>> a
{1, 2, 3, 4, 5}
>>> a = {1, 2, 3, 4}
>>> a.update({5})
>>> a
{1, 2, 3, 4, 5}
```
```&=```은 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장하며 intersection_update 메서드와 같습니다. 
- 세트1 &= 세트2
- 세트1.intersection_update(세트2)
```
>>> a = {1, 2, 3, 4}
>>> a &= {0, 1, 2, 3, 4}
>>> a
{1, 2, 3, 4}
>>> a = {1, 2, 3, 4}
>>> a.intersection_update({0, 1, 2, 3, 4})
>>> a
{1, 2, 3, 4}
```
```-=```은 현재 세트에서 다른 세트를 빼며 difference_update 메서드와 같습니다.
- 세트1 -= 세트2
- 세트1.difference_update(세트2)
```
>>> a = {1, 2, 3, 4}
>>> a -= {3}
>>> a
{1, 2, 4}
>>> a = {1, 2, 3, 4}
>>> a.difference_update({3})
>>> a
{1, 2, 4}
```
```^=```은 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장하며 symmetric_difference_update 메서드와 같습니다.
- 세트1 ^= 세트2
- 세트1.symmetric_difference_update(세트2)
```
>>> a = {1, 2, 3, 4}
>>> a ^= {3, 4, 5, 6}
>>> a
{1, 2, 5, 6}
>>> a = {1, 2, 3, 4}
>>> a.symmetric_difference_update({3, 4, 5, 6})
>>> a
{1, 2, 5, 6}
```

### 26.2.2  부분 집합과 상위집합 확인하기
```<=```은 현재 세트가 다른 세트의 부분집합(subset)인지 확인하며 issubset 메서드와 같습니다.

- 현재세트 <= 다른세트
- 현재세트.issubset(다른세트)
```
>>> a = {1, 2, 3, 4}
>>> a <= {1, 2, 3, 4}
True
>>> a.issubset({1, 2, 3, 4, 5})
True
```
<details>
<summary>[그림 26-5] 세트가 부분집합인지 확인
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13737/mod_page/content/3/026005.png)
</div>
</details>

```<```은 현재 세트가 다른 세트의 진부분집합(proper subset)인지 확인하며 메서드는 없습니다.
- 현재세트 < 다른세트
```
>>> a = {1, 2, 3, 4}
>>> a < {1, 2, 3, 4, 5}
True
```

<details>
<summary>[그림 26-6] 세트가 진부분집합인지 확인
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13737/mod_page/content/3/026006.png)
</div>
</details>

```>=```은 현재 세트가 다른 세트의 상위집합(superset)인지 확인하며 issuperset 메서드와 같습니다.
- 현재세트 >= 다른세트
- 현재세트.issuperset(다른세트)
```
>>> a = {1, 2, 3, 4}
>>> a >= {1, 2, 3, 4}
True
>>> a.issuperset({1, 2, 3, 4})
True
```

<details>
<summary>[그림 26-7] 세트가 상위집합인지 확인
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13737/mod_page/content/3/026007.png)
</div>
</details>

```>```은 현재 세트가 다른 세트의 진상위집합(proper superset)인지 확인하며 메서드는 없습니다.

- 현재세트 > 다른세트
```
>>> a = {1, 2, 3, 4}
>>> a > {1, 2, 3}
True
```

<details>
<summary>[그림 26-8] 세트가 진상위집합인지 확인
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13737/mod_page/content/3/026008.png)
</div>
</details>

### 26.2.3  세트가 같은지 다른지 확인하기
```== 연산자```를 사용하여 서로 같은지 확인
```
>>> a = {1, 2, 3, 4}
>>> a == {1, 2, 3, 4}
True
>>> a == {4, 2, 1, 3}
True
```
```!= 연산자```는 세트가 다른지 확인
```
>>> a = {1, 2, 3, 4}
>>> a != {1, 2, 3}
True
```
### 26.2.4  세트가 겹치지 않는지 확인하기
```disjoint```는 현재 세트가 다른 세트와 겹치지 않는지 확인 
- 현재세트.isdisjoint(다른세트)
```
>>> a = {1, 2, 3, 4}
>>> a.isdisjoint({5, 6, 7, 8})       # 겹치는 요소가 없음
True
>>> a.isdisjoint({3, 4, 5, 6})    # a와 3, 4가 겹침
False
```
## 26.3 세트 조작하기

### 26.3.1  세트에 요소 추가하기
**add(요소)** 는 세트에 요소를 추가
```
>>> a = {1, 2, 3, 4}
>>> a.add(5)
>>> a
{1, 2, 3, 4, 5}
```
### 26.3.2  세트에서 특정 요소를 삭제하기
**remove(요소)** 는 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생
```
>>> a.remove(3)
>>> a
{1, 2, 4, 5}
```
**discard(요소)** 는 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어감
```
>>> a.discard(2)
>>> a
{1, 4, 5}
>>> a.discard(3)
>>> a
{1, 4, 5}
```

### 26.3.3  세트에서 임의의 요소 삭제하기
**pop()** 은 세트에서 임의의 요소를 삭제하고 해당 요소를 반환
```
>>> a = {1, 2, 3, 4}
>>> a.pop()
1
>>> a
{2, 3, 4}
```
### 26.3.4  세트의 모든 요소를 삭제하기
**clear()**는 세트에서 모든 요소를 삭제
```
>>> a.clear()
>>> a
set()
```
### 26.3.5  세트의 요소 개수 구하기
```
>>> a = {1, 2, 3, 4}
>>> len(a)
4
```
## 26.6 세트 표현식 사용하기

- {식 for 변수 in 반복가능한객체}
- set(식 for 변수 in 반복가능한객체)
```
>>> a = {i for i in 'apple'}
>>> a
{'l', 'p', 'e', 'a'}
```

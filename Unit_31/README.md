# Unit 31. 함수에서 재귀호출 사용하기
함수 안에서 함수 자기자신을 호출하는 방식을 **재귀호출(recursive call)**이라고 한다.

## 31.1 재귀호출 사용하기
먼저 간단한 재귀호출 함수를 만들어보겠습니다. 
```
def hello():
    print('Hello, world!')
    hello()
 
hello()
```
hello 함수 안에서 다시 hello 함수를 호출하고 있습니다.
hello 함수가 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면 RecursionError가 발생합니다.

<details>
<summary>[그림 31-1] 재귀호출과 스택 넘침 현상
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13846/mod_page/content/3/031001.png)
</div>
</details>

### 31.1.1  재귀호출에 종료 조건 만들기
재귀호출을 사용하려면 반드시 다음과 같이 종료 조건을 만들어주어야 합니다.

```
def hello(count):
    if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return
    
    print('Hello, world!', count)
    
    count -= 1      # count를 1 감소시킨 뒤
    hello(count)    # 다시 hello에 넣음
 
hello(5)    # hello 함수 호출
```
## 31.2 재귀호출로 팩토리얼 구하기

```
def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 
print(factorial(5))
```

<details>
<summary>[그림 31-3] factorial 함수
</summary>
<div markdown="1">       

😎

그림 31-3 factorial 함수의 호출
![](https://dojang.io/pluginfile.php/13847/mod_page/content/2/031003.png)

그림 31-4 factorial 함수의 반환
![](https://dojang.io/pluginfile.php/13847/mod_page/content/2/031004.png)

그림 31-5 factorial 함수의 호출 순서와 계산 과정
![](https://dojang.io/pluginfile.php/13847/mod_page/content/2/031005.png)

</div>
</details>
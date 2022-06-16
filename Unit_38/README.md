# Unit 38. 예외 처리 사용하기
## 38.1 try except로 사용하기
```
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
```

<details>
<summary>[그림 38-1] 예외 발생과 except
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13945/mod_page/content/2/038001.png)

</div>
</details>

## 38.2 else와 finally 사용하기
```
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
```

```
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
```

### 38.2.1  예외와는 상관없이 항상 코드 실행하기
```
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드
```

<details>
<summary>[그림 38-3] try, except, else, finally의 실행 과정
</summary>
<div markdown="1">       

😎

![](https://dojang.io/pluginfile.php/13946/mod_page/content/3/038003.png)

</div>
</details>

## 38.3 예외 발생시키기
- raise 예외('에러메시지')
```
try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)
-----------------------------------------------------------------------------
실행 결과
3의 배수를 입력하세요: 5 (입력)
예외가 발생했습니다. 3의 배수가 아닙니다.
```


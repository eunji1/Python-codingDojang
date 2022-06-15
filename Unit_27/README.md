# Unit 27. 파일 사용하기
## 27.1 파일에 문자열 쓰기, 읽기
### 27.1.1  파일에 문자열 쓰기
파일에 문자열을 쓸 때는 open 함수로 파일을 열어서 파일 객체(file object)를 얻은 뒤에 write 메서드를 사용합니다.

- 파일객체 = open(파일이름, 파일모드)
- 파일객체.write('문자열')
- 파일객체.close()
```
file_write_string.py
file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')      # 파일에 문자열 저장
file.close()                     # 파일 객체 닫기
```
### 27.1.2  파일에서 문자열 읽기
파일을 읽을 때도 open 함수로 파일을 열어서 파일 객체를 얻은 뒤 read 메서드로 파일의 내용을 읽습니다. 단, 이때는 파일 모드를 읽기 모드 'r'로 지정합니다.

- 변수 = 파일객체.read()
```
file_read_string.py
file = open('hello.txt', 'r')    # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기
```
### 27.1.3  자동으로 파일 객체 닫기
파이썬에서는 with as를 사용하면 파일을 사용한 뒤 자동으로 파일 객체를 닫아줍니다. 다음과 같이 with 다음에 open으로 파일을 열고 as 뒤에 파일 객체를 지정합니다.
```
with open(파일이름, 파일모드) as 파일객체:
    코드
```
## 27.2 문자열 여러 줄을 파일에 쓰기, 읽기

### 27.2.1  반복문으로 문자열 여러 줄을 파일에 쓰기
```
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
```
파일에 문자열 여러 줄을 저장할 때 주의할 부분은 개행 문자 부분입니다. 'Hello, world! {0}\n'와 같이 문자열 끝에 개행 문자 \n를 지정해주어야 줄바꿈이 됩니다. 

## 27.2.2  리스트에 들어있는 문자열을 파일에 쓰기

- 파일객체.writelines(문자열리스트)
```
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
 
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)
```
### 27.2.3  파일의 내용을 한 줄씩 리스트로 가져오기
- 변수 = 파일객체.readlines()
```
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)
```
### 27.2.4  파일의 내용을 한 줄씩 읽기
- 변수 = 파일객체.readline()
```
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
```
readline으로 파일을 읽을 때는 while 반복문을 활용

## 27.3 파이썬 객체를 파일에 저장하기, 가져오기
파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공

<details>
<summary>[그림 27-3] 피클링과 언피클링
</summary>
<div markdown="1">       
다음과 같이 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)이라고 하고, 파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 합니다.

😎
![](https://dojang.io/pluginfile.php/13766/mod_page/content/3/027003.png)
</div>
</details>

### 27.3.1  파이썬 객체를 파일에 저장하기
그럼 파이썬 객체를 파일에 저장하는 피클링을 해보겠습니다. 피클링은 pickle 모듈의 dump 메서드를 사용

```
import pickle
 
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
 
with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
```
특히 pickle.dump로 객체(값)를 저장할 때는 open('james.p', 'wb')와 같이 파일 모드를 'wb'로 지정해야 함 
- b는 바이너리(binary)를 뜻하는데, 바이너리 파일은 컴퓨터가 처리하는 파일 형식

### 27.3.2  파일에서 파이썬 객체 읽기
파일에서 파이썬 객체를 읽어오는 언피클링  
- 언피클링은 pickle 모듈의 load 사용 
- 파일 모드를 바이너리 읽기 모드 'rb'로 지정

<details>
<summary>[그림 27-4] 파일 모드 조합
</summary>
<div markdown="1">       

😎
![](https://dojang.io/pluginfile.php/13766/mod_page/content/3/027004.png)
</div>
</details>
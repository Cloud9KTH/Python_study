# Python study



## 01 파이썬 프로그래밍 언어





## 02 파이썬 시작하기







## 03 파이썬을 계산기 처럼 활용하기









## 04 변수와 자료형





#### 01 변수





#### 02 문자열





#### 03 리스트

(1, 2, 3, 'apple', 'fox')



#### 04 튜플





#### 05 세트



#### 06 딕셔너리

{key1:value1, key2:value2, key3:value3,.....}



## 05 제어문

> 코드의 특정 부분만 수행하거나 반복 가능. 코드의 진행 순서를 바꾸는 구문을 제어문 이라고 함. 제어문에는 조건을 검사해 분기하는 구문인 조건문과 어떤 구간이나 조건을 만족하는 동안 코드의 일부분을 반복하는 구문인 반복문이 있음. 제어문을 이용하면 상황에 따라 다르게 코드를 실행할 수 있어서 프로그램이 지능이 있는 기기 처럼 동작하도록 만들 수 있음. 조건문과 반복문 학습

#### 01 조건에 따라 분기하는 if 문

**단일 조건에 따른 분기(if)**

```python
if <조건문> :
	<코드 블록>
```

if 문에서 <조건문>을 만족하면(참이면)  <코드 블록> 수행. 만족하지 않으면 수행하지 않음.  <조건문> 다음에 **콜론(:)** 입력. 다음줄에서 <코드 블록> 작성할 때, **들여쓰기**를 **꼭** 해야함. 들여쓰기 할 때, **탭(tab)** 이나 **스페이스바**로 **네칸** 을 들여씀.

※ 들여쓰기는 **탭** 이나 **스페이스바 네칸**을 **섞어 쓰면 안됌**. 들여쓰기가 잘못 되면 오류가 발생하기 때문에 한종류로만 쓸것. 보통의 개발도구(Visual studio code, Jupyter notebook, 등등) 에서는 콜론(:) 입력후 enter를 누르면 자동으로 들여쓰기가 됌.

▷ 비교 연산자

| 비교 연산자 | 의미        | 활용 예 | 설명                  |
| ----------- | ----------- | ------- | --------------------- |
| ==          | 같다        | a == b  | a는 b와 같다          |
| !=          | 같지 않다   | a != b  | a는 b와 같지 않다     |
| <           | 작다        | a < b   | a는 b보다 작다        |
| >           | 크다        | a > b   | a는 b보다 크다        |
| <=          | 작거나 같다 | a <= b  | a는 b보다 작거나 같다 |
| >=          | 크거나 같다 | a >= b  | a는 b보다 크거나 같다 |



▷ 논리 연산자

| 논리 연산자 | 의미     | 활용 예 | 설명                                                |
| ----------- | -------- | ------- | --------------------------------------------------- |
| and         | 논리곱   | A and B | A와 B가 모두 참이고 그 외에는 거짓                  |
| or          | 논리합   | A or B  | A와 B 중 하나라도 참이면 참이고 둘 다 거짓이면 거짓 |
| not         | 논리부정 | not A   | A가 참이면 거짓이고 거짓이면 참                     |



if 문 활용 실제 예시<단일 조건>

````python
x = 95
if x > 90:
	print('pass')
````

`Out`: pass



**단일 조건 및 그 외 조건에 따른 분기(if~else)**

```python
if <조건문>:
    <코드 블록 1>
else:
    <코드 블록 2>
```



if~else 문 실제 예시

```python
x = 75
if x >= 90 :
	print('pass')
else:
    print('fail')
```

`Out`: fail



**여러 조건에 따른 분기(if~elif~else)**

> 여러 조건 구문에서 **elif** 는 **여러개 사용 가능. **
>
> if 문 에서 **else 문**은 **꼭 안써도 상관 없음.**

```python
if <조건문 1>:
    <코드 블록 1>
elif <조건문 2>:
    <코드 블록 2>
       .
       .
       .
elif <조건문 n>:
    <코드 블록 n>
else:
    <코드 블록 m>    
```



if~elif~else 문 실제 예시

```python
x = 85
if x >= 90:
    print('very good')
elif 80 <= x < 90:
    print('good')
else:
    print('bad')
```

`Out`: good



**중첩 조건에 따른 분기**

> <코드 블록>에 또 다른 조건문 포함 가능.

```python
if <조건문 1>:
    if <조건문 1-1>:
        <코드 블록 1-1>
    else:
        <코드 블록 1-2>
elif <조건문 2>:
    <코드 블록 2>
else:
    <코드 블록 3>
```



중첩 조건문 실제 예시

```python
x = 100
if x >= 90:
    if x == 100:
        print('perfect')
    else:
        print('very good')
elif 80 <= x < 90:
    print('good')
else:
    print('bad')
```

`Out`: perfect

※ 코드를 작성하다 보면 우선 전체적인 구조만 먼저 잡고 나중에 상세 실행 코드를 구현 하는것이  편할 때가 있음. 그때 활용할 수 있는 것이 `pass`임. 예로 if 문에서 세부 실행 조건이나 조건문을 `pass`로 채워 두면 아무 일도 일어나지 않음. 전체적인 구조를 잡을 때 아무것도 쓰지 않으면 오류가 발생함.



#### 02 지정된 범위만큼 반복하는 for 문

**반복문의 필요성**

같은 코드를 변수만 조금 바꿔 수백~수천~수만 번 반복해서 작성하는 것은 비 효율적임.



**for 문의 구조**

```python
for <반복 변수> in <반복 범위>:
	<코드 블록>
```

**반복 범위 지정**

###### 리스트 이용

실제 예시

```python
for a in [0, 1, 2, 3, 4, 5]:      
	print(a)
```

`Out`: 0

​		  1

​		  2

​		  3

​		  4

​		  5



```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']    # 리스트를 변수에 할당
for myFriend in myFriends:
    print(myFriend)
```

`Out`: James

​		  Robert

​		  Lisa

​		  Mary



###### range() 함수 이용

```python
range(start, stop, step)     # stop은 포함되지 않음. (ex: stop에 8을 지정하면 7까지)
                             # step은 반복 범위
```



```python
print(list(range(0, 10, 1)))
```

`Out`: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

※ range() 함수로 생성된 범위는 start 에서 stop 전까지 생성 됨.

````python
for a in range(0, 6, 1):
	print(a)
````

`Out`: 0

​		  1

​		  2

​		  3

​		  4

​		  5



```
for a in range(0, 6, 2):
	print(a)
```

`Out`: 0

​		  2

​		  4



**※ step 이 1인 경우, step 생략 가능**

```python
range(Start, stop)
```

**※ step 이 1이고, start 가 0인 경우, start, step 생략하고 stop 만 지정 가능.**

```python
range(stop)
```



```python
print(list(range(0, 10, 1)))
print(list(range(0, 10)))
print(list(range(10)))
```

`Out`: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

​		  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

​		  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
print(list(range(0, 20, 5)))
print(list(range(-10, 0, 2)))
print(list(range(3, -10, -3)))
print(list(range(0, -5, 1)))
```

`Out`: [0, 5, 10, 15]

​		  [-10, -8, -6, -4, -2]

​		  [3, 0, -3, -6, -9]

​		  []



**중첩 for 문**

```python
for <반복 변수 1> in <반복 범위 1>:
	for <반복 변수 2> in <반복 범위 2>:
		<코드 블록>
```



```python
x_list = ['x1', 'x2']
y_list = ['y1', 'y2']

print('x y')
for x in x_list:
    for y in y_list:
        print(x, y)
```

`Out`: x y

​		x1 y1

​		x1 y2

​		x2 y1

​		x2  y2



**여러 개의 리스트 다루기**

```python
names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]
for k in range(len(names)):
	print(names[k], scores[k])
```

`Out`: James 95

​		  Robert 96

​		  Lisa 97

​		  Mary 94

**※ `len()` 함수는 리스트의 길이(항목 개수)를 확인 하는 함수.**



zip 함수 구조

```python
for var1, var2 in zip(list1, list2):
	<코드 블록>
```

zip() 함수를 이용해 for 문을 구성하면 <반복 범위>인 zip() 안에 있는 list1과 list2의 항목이 각각 순서대로 동시에 <반복 변수>인 var1, var2에 대입디고 <코드 블록>을 수행.

실제 예시

```python
names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]
for naem, score in zip(naems, scores):
    print(naems, score)    
```

`Out`: James 95

​		  Robert 96

​		  Lisa 97

​		  Mary 94



#### 03 조건에 따라 반복하는 while 문

**while 문의 구조**

```python
while <조건문>: 
	<코드 블록>
```



```python
i = 0                # 초기화
sum = 0              # 초기화

print('i sum')
while (sum < 20):    # 조건 검사
    i = i + 1        # i를 1 씩 증가
    sum = sum + i    # 이전의 sum과 현재 i를 더해 sum 갱신
    print(i, sum)    # i와 sum을 출력
```

`Out`: i sum

​		  1 1 

​		  2 3 

​		  3 6 

​		  4 10 

​		  5 15 

​		  6 21



**무한 반복 while 문**

```python
while Ture:
    print("while test")
```

조건문이 항상 참일 경우 <코드 블록>에 있는 코드가 무한 반복 되므로 주의가 필요. 중지 시키려면 주피터 노트북에서는 툴바의 [커널 정지(interrupt the kernel)] 아이콘을 누르고 파이썬 콘솔이나 Ipython 콘솔에서는 `Ctrl + C`를 누름.



#### 04 반복문을 제어하는 break와 continue

> for, while 반복문 에서 반복을 멈추고 <코드 블록>을 빠져 나오거나 다음 반복을 수생하게 하려면 **break** 와 **continue** 사용.

**반복문을 빠져나오는 break**

```python
k = 0
while True:
    k = k + 1     # k는 1씩 증가
    if (k > 3):   # K가 3보다 크면
        break     # break로 while 문을 빠져나옴
    print(K)      # k 출력
```

`Out`: 1

​		  2

​		  3



```python
for k in range(10):
    if(k > 2):     # k가 2보다 크면
        break      # break로 for 문을 빠져나옴
    print(K)       # k 출력
```

`out`: 0

​		  1

​		  2



**다음 반복을 실행하는 continue**

```python
for k in range(5):
    if(k == 2):
        continue
    print(k)
```

`Out`: 0

​		  1

​		  3

​		  4

※ k 가 2일 때 지정 조건을 만족해 continue가 실행돼 반복문의 처음으로 돌아가서 다음 반복을 진행 하므로 continue 다음에 있는 `print(k)`는 실행되지 않음.



```python
k = 0
while True:
    k = k + 1
    if(k == 2): 
        print('continue next')
        continue
    if(k > 4):
        break
    print(k)
```

`Out`: 1 

​		  continue next 

​		  3 

​		  4



#### 05 간단하게 반복하는 한 줄 for 문





**제어문 연습**

if 



한국 나이 --> 미국 나이 변환기 코드

```python
age = input("How old are you?")
check = input("Did you pass your birthday? Please answer \"O\" or \"X\"")
if check == 'O':
    print (int(age)-1)
elif check == 'X':
    print (int(age)-2)
else :
	print ('Repeat again~!!')

```







for



for 조건문을 활용한 카운트 다운 코드

```python
a = int(input('카운트 다운하고 싶은 초기 숫자 입력 -->'))
for b in range(a, 0, -1) :
  print(b)
print('발사')
```



for 조건문을 활용한 곱셈표 생성기. (2~9단 까지만...)

```python
print('곱셈 표 생성')
for a in range(2, 10) :
  print (a, '단')
  for b in range(1, 10):
    print(a, 'X', b, '=', a*b)
```



for 조건문을 활용한  점수 출력 코드

`len()` 함수와 `range()` 함수가 익숙하지 않아 이상한 결과값을 많이 출력하고 디버깅 하다가 원하는 형태의 코드로 변경 함. 

* 디버깅 할때  (**#**) 을 많이 활용하고 그냥 냅다 실행해서 결과값을 확인했다.
* **#** 활용은 잘한거 같지만, 냅다 실행한건 좋은 디버깅 습관은 아닌거 같다.



* 실행은 되지만, 원하는 결가 값이 나오지 않은 실패작 코드

```python
a = ('다니엘', '제임스','피터', '칼')
#b = ('데이브', '아놀드', '헤레이스')
c = ('업무태도', '성과', '친화력', '고객응대')
d = (95, 90, 88, 83)
#e = (75, 80, 78, 87)
#f= (63, 30, 50, 30)

for i in range(len(a)) :
  for j in range(len(c)):
    for k in range(len(d)):
      print(a[j],'의', c,) ###'평가 결과는', d[k])
##print (a[i] '의' c[i] '평가 결과는', d[i])
```



* 디버깅에 성공해서 원하는 결과를 출력한 코드

```python
n = ('다니엘', '제임스','피터', '칼')
item = ('업무태도', '성과', '친화력', '고객응대')
s = (95, 90, 88, 83)
for k in range (len(n)):
  for j in range(len(item)) :
    print(n[k],'의', item[j],'점수는', s[j])
```









while



while 구문을 활용한 카운트 다운 코드.

```python
a = int(input('카운트 다운 숫자 써봐'))
while True :
  a = a-1
  print (a)

  if a == 0 :
    break
```







## 06 입력과 출력

#### 01 화면 출력

**기본 출력**

```python
print("Hello Python!!")
```

`Out`: Hello Python!!









**형식 지정 출력**





```python
ani_0 = 'cat'
ani_1 = 'fox'
ani_2 = 'dog'
ani_3 = 'cow'

print("animal: {0},{3}".format(ani_0,ani_1,ani_2, ani_3))
```







#### 03 파일 읽고 쓰기

**파일 열기**

`open()` 함수 사용.

`f = open('file_name', 'mode')` 형태로 사용.

| mode | 의미                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 읽기 모드로 파일 열기(기본), 모드를 지정하지 않으면 기본적으로 읽기 모드로 지정됨 |
| w    | 쓰기 모드로 파일 열기, 같은 이름의 파일이 있으면 기존 내용은 모두 삭제됨 |
| x    | 쓰기 모드로 파일 열기, 같은 이름의 파일이 있을 경우 오류가 발생함 |
| a    | 추가 모드로 파일 열기, 같은 이름의 파일이 없으면 w와 기능 같음 |
| b    | 바이너리 파일 모드로 파일 열기                               |
| t    | 텍스트 파일 모드로 파일 열기(기본), 지정하지 않으면 기본적으로 텍스트 모드로 지정됨 |

※ mode에 아무것도 쓰지 않으면 'rt' 기능을 함.



**파일 쓰기**

> 파일  쓰기를 하려면 우선 파일을 쓰기 모드로 열어야 함. 파일이 테스트 파일인지 바이너리 파일인지도 지정할 수 있음. 특별히 지정하지 않으면 기본적으로 텍스트 파일 모드로 파일을 열게 됨. 파일을 열고 저장한 내용을 쓴 후에는 파일을 닫아야 함. 

파일 쓰기를 위한 코드의 구조

```python
f = open('file_name', 'w')
f.write(str)
f.close()
```



실제 예시

```python
f = open('myFile.txt', 'w')          # (1) 'myFile.txt' 파일 쓰기 모드로 열기
f.write('This is my first file')     # (2) 연 파일에 문자열 쓰기
f.close()                            # (3) 파일 닫기
```

윈도우 커맨드 창(`cmd`) 에서 `type myFile.txt` 입력하면 입력된 문자열(This is my first file)이 출력됨.



**파일 읽기**

> 파일을 읽으려면 파일을 읽기 모드로 열어야 함. 그 후 파일의 내용을 읽고 마지막으로 파일을 닫음.

파일을 읽기 위한 코드의 구조

```python
f = open('file_name', 'r')      # f = open('file_name')도 가능
data = f.read()
f.close()
```



실제 예시

```python
f = open('myFile.txt', 'r')      # (1) 'myFile.txt' 파일 읽기 모드로 열기
file_text = f.read()             # (2) 파일 내용 읽은 후에 변수에 저장
f.close()                        # (3) 파일 닫기

print(file_text)                 # 변수에 저장된 내용 출력
```

`Out`: Ths is my first file.



#### 04 반복문을 이용해 파일 읽고 쓰기

> 텍스트 파일의 데이터를 읽거나 데이터를 텍스트 파일로 쓸 때 반복문을 이용해 파일의 내용을 한 줄씩 처리해야 할 때가 많음. 

**파일에 문자열 한 줄씩 쓰기**

> for 문을 이용해 문자열을 한 줄씩 파일에 쓰는 방법. 먼저 파일을 연 후에 for 문에서 지정된 범위만큼 반복해서 문자열을 한 줄씩 파일에 쓰고 마지막으로 파일을 닫음.

구구단 2단의 일부를 파일로 저장하는 코드.

```python
f = open('two_times_table.txt', 'w')          # (1) 파일을 쓰기 모드로 열기
for num in range(1, 6) :                      # (2) for 문: num이 1~5까지 반복
	format_string = "2 X {0} = {1}\n".format(num, 2*num) # 저장할 문자열 생성
	f.write(format_string)                    # (3) 파일에 문자열 저장
f.close()                                     # (4) 파일 닫기
```

`cmd`: type two_times_table.txt

`Out`: 2 X 1 = 2

​          2 X 2 = 4

​          2 X  3 = 6

​		  2 X 4 = 8 

​		  2 X 5 = 10

**파일에서 문자열 한 줄씩 읽기**

> 지금 까지 `f = open('file_name')` 으로 파일을 연 후 `f.read()`를 이용해 파일 내용을 읽었음. 파일 내용 전체를 반환하므로 내용을 한줄 씩 읽어서 처리할때 사용이 어려움. 파일 내용을 한줄 씩 읽고 처리하려면 `readline()` 또는 `readlines()`를 써야 함.

readline()

파일을 연 후 readline()을 수행하면 파일로부터 문자열 한줄을 읽음. 다시 readline()을 실행하면 바로 그 다음 문자열 한줄을 읽음. 이런식으로 readline()은 실행한 횟수만큼 문자열을 한줄씩 읽음. 만약 파일의 마지막 한 줄을 읽고 나서 다시 readline()을 수행하면 빈 문자열을 반환함.

실제 예시

```python
f = open('two_times_table.txt')     # 파일을 읽기 모드로 열기
line1 = f.readline()                # 한 줄씩 문자열을 읽기
line2 = f.readline()
f.close()                           # 파일 닫기
print(line1, end=" ")               # 한 줄씩 문자열 출력(줄 바꿈 안함)
print(line2, end=" ")
```

`Out`: 2 X 1 = 2

​		  2 X 2 = 4

`end = " "`: 줄 바꿈 안하는 명령어



while 문을 활용한 readline() 예시

> `while line:`에서 line이 빈 문자열인지 검사해서 빈 묹열이 아니면 while 문 계속 실행. 빈 문자열이면 while 문 빠져 나옮.

```python
f = open('two_times_table.txt')    # 파일을 읽기 모드로 열기
line = f.readline()                # 문자열 한 줄 읽기
while line:                        # line이 공백인지 검사해서 반목 여부 결정
	print(line, end=" ")           # 문자열 한줄 출력(줄 바꿈 안함)
	line = f.readline()            # 문자열 한 줄 읽기
f.close()                          # 파일 닫기
```

`Out`: 2 X 1 = 2

​          2 X 2 = 4

​          2 X  3 = 6

​		  2 X 4 = 8 

​		  2 X 5 = 10



readlines()

> readline()은 파일에서 문자열을 한줄씩 읽었지만 readlines()는 파일 전체의 모든 줄을 읽어 한줄씩을 요소로 갖는 리스트 타입으로 반환.

실제 예시

```python
f = open('two_times_table.txt')    # (1) 파일을 읽기 모드로 열기
lines = f.readlines()              # (2) 파일 전체 읽기(리스트로 반환)
f.close()                          # (3) 파일 닫기

print(lines)                       # 리스트 변수 내용 출력
```

`Out`: '2 X 1 = 2\n', '2 X 2 = 4\n', '2 X  3 = 6\n', '2 X 4 = 8\n', '2 X 5 = 10\n', ........



for 문을 활용한 readlines() 예시

```python
f = open('two_times_table.txt')    # 파일을 읽기 모드로 열기
lines = f.readlines()              # 파일 전체 읽기(리스트로 반환)
f.close()                          # 파일 닫기
for line in lines :                # 리스트를 <반복 밤위>로 지정
    print(line, end=" ")           # 리스트 항목을 출력(줄 바꿈 안함)
```

`Out`: 2 X 1 = 2

​          2 X 2 = 4

​          2 X  3 = 6

​		  2 X 4 = 8 

​		  2 X 5 = 10



위 코드의 단축 버전

```python
f = open('two_times_table.txt')    # 파일을 읽기 모드로 열기
for line in f.readlines():         # 파일 전체를 읽고, 리스트 항목을 line에 할당 
    print(line, end=" ")           # 리스트 항목을 출력(줄 바꿈 안함)
f.close()                          # 파일 닫기
```

`Out`: 2 X 1 = 2

​          2 X 2 = 4

​          2 X  3 = 6

​		  2 X 4 = 8 

​		  2 X 5 = 10



위 코드의 단축 버전

```python
f = open('two_times_table.txt')    # 파일을 읽기 모드로 열기
for line in f:                     # 파일 전체를 읽고, 리스트 항목을 line에 할당 
    print(line, end=" ")           # 리스트 항목을 출력(줄 바꿈 안함)
f.close()                          # 파일 닫기
```

`Out`: 2 X 1 = 2

​          2 X 2 = 4

​          2 X  3 = 6

​		  2 X 4 = 8 

​		  2 X 5 = 10



#### 05 with 문을 활용해 파일 읽고 쓰기

**with 문의 구조**

> with 문을 활용할 경우, 수행이 끝난 후에 자동으로 파일을 닫기 때문에 close()를 쓰지 않아도 됨.

with 문 활용시 코드 구조

```python
with open('file_name', 'mode') as f:
    <코드 블록>
```

with 문 활용시 **쓰기(w)** 예시

```python
with open('file_name', 'w') as f:
    f.write(str)
```

with 문 활용시 **읽기(r)** 예시

```python
with open('file_name', 'r') as f:
    data = f.read()
```



**with 문의 활용**

문자열 쓰는 예시

```python
with open('C:/myPycode/myTextfile2.txt', 'w') as f:   # (1) 파일 열기
    f.write('File read/write test2: line1\n')         # (2) 파일 쓰기
    f.write('File read/write test2: line2\n')
    f.write('File read/write test2: line3\n')
```

읽기 예시

```python
with open('C:/myPycode/myTextfile2.txt', 'w') as f:   # (1) 파일 열기
    file_string = f.read()                            # (2) 파일 읽기
	print(file_string)
```

`Out`: File read/write test2: line1

​		  File read/write test2: line2

​		  File read/write test2: line3



with 문을 활용한 구구단 3단 일부 만들기 프로그램 예시

```python
with open('C:/myPycode/myTextfile3.txt', 'w') as f:         # 파일 쓰기 모드로 열기
    for num in range(1, 6) :                                # for 문에서 num이 1~5까지 반복
        format_string = "3 X {0} = {1}\n".format(num, 3*num)# 문자열 생성
        f.write(format_string)                              # 파일에 문자열 쓰기
```

with 문을 활용한 구구단 3단 일부 출력 프로그램 예시

```python
with open('C:/myPycode/myTextfile3.txt', 'r') as f:      # 파일 읽기 모드로 열기
    for line in f:                              # 파일 전체를 읽고 리스트 항목을 line에 할당
        print(line, end=" ")                    # line에 할당된 문자열 출력(줄 바꿈 안함)
```


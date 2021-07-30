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

*** 단일 조건에 따른 분기(if)**

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



*** 단일 조건 및 그 외 조건에 따른 분기(if~else)**

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



*** 여러 조건에 따른 분기(if~elif~else)**

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



*** 중첩 조건에 따른 분기**

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

*** 반복문의 필요성**

같은 코드를 변수만 조금 바꿔 수백~수천~수만 번 반복해서 작성하는 것은 비 효율적임.



*** for 문의 구조**

```python
for <반복 변수> in <반복 범위>:
	<코드 블록>
```

*** 반복 범위 지정**

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



*** 중첩 for 문**

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



*** 여러 개의 리스트 다루기**

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

*** while 문의 구조**

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



*** 무한 반복 while 문**

```python
while Ture:
    print("while test")
```

조건문이 항상 참일 경우 <코드 블록>에 있는 코드가 무한 반복 되므로 주의가 필요. 중지 시키려면 주피터 노트북에서는 툴바의 [커널 정지(interrupt the kernel)] 아이콘을 누르고 파이썬 콘솔이나 Ipython 콘솔에서는 `Ctrl + C`를 누름.



#### 04 반복문을 제어하는 break와 continue

> for, while 반복문 에서 반복을 멈추고 <코드 블록>을 빠져 나오거나 다음 반복을 수생하게 하려면 **break** 와 **continue** 사용.

*** 반복문을 빠져나오는 break**

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



*** 다음 반복을 실행하는 continue**

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

> 파이썬에서는 리스트, 세트, 딕셔너에서 실행할 수 있는 한 줄 for 문도 지원. 각각 ‘리스트 컴프리헨션(List comprehension)’, ‘세트 컴프리헨션(Set  comprehension)’, ‘딕셔너리 컴프리 헨션(Dictionary comprehension)’  이라고 함. 컴프리헨션(Comprehension)은 우리말로 내포 (혹은 내장)라는 뜻으로서 리스트, 세트, 딕셔너리 컴프리헨션은 각각 리스트, 세트, 딕셔너리내에 코드 가 내포돼 실행되는 것을 의미. 컴프리헨션을 잘 이용하면 리스트, 세트, 딕셔너리 데이터를 반복해서 처리 해야 할 때 코드를 한 줄로 작성할 수 있어서 편리.

*** 리스트 컴프리헨션의 기본 구조**

```python
[〈반복 실행문〉 for <반복 변수> in 〈반복 범위〉]
```

 for 문에서는 〈반복 실행문〉이 `for 〈반복 변수〉 in <반복 범위>:` 다음 줄에 왔는데 **한 줄 for 문에서는 <반복 실행문>이 먼저 나옴**. **콜론(:)도 이용하지 않음.**

```python
numbers = [1, 2, 3, 4, 5]
square = []

for i in numbers:
	square.append(i**2)
	
print(square)
```

`Out`: [1, 4, 9, 16, 25]

```python
numbers = [1, 2, 3, 4, 5]
square = [i**2 for i in numbers]
print(square)
```

`Out`: [1, 4, 9, 16, 25]

*** 조건문을 포함한 리스트 컴프리헨션**

리스트 컴프리헨션은 for 문 다음에 if <조건문>을 추가할 수 있음. 

```python
[반복 실행문〉 for <반복 변수〉 in <반복 범위〉 if <조건문>]
```

반복문을 수행하다가 if 〈조건문>을 만족하는 경우에만 <반복 실행문> 을 실행.

```python
numbers = [1, 2, 3, 4, 5]
square = []

for i in numbers:
    if i >= 3:
        square.append(i**2)
	
print(square)
```

`Out`: [9, 16, 25]

```python
numbers = [1, 2, 3, 4, 5]
square = [i**2 for i in numbers if i >= 3]

print(square)
```

`Out`: [9, 16, 25]



**제어문 연습**

▷ if 

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



▷ for

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



▷ while

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

*** 기본 출력**

```python
print("Hello Python!!")
```

`Out`: Hello Python!!

```python
print("Best", "python", "book")
```

`Out`: Best python book

※ 문자열 여러 개를 연결해 출력하려면 문자열을 콤마(,)로 구분하고 연속 해서 입력. 콤마로 구분 하면 출력에서 자동으로 빈칸(공백)이 하나씩 들어감.

```python
print("Best", "python", "book", sep = "-:*:-")
```

`Out`: Best-:*:-python-:*:-book

※ 빈칸 대신 다른 문자열을 넣으려면 print() 함수 안에 두 문자열 사이의 구분하는 값을 설정하는 sep 인자를 이용 . print()함수에서 sep 인자를 지정하지 않으면 기본적으로 빈칸이 들어감. 빈칸을 다른 문자열로 바꾸려면 ‘sep = 문자열'을 추가.

```python
print("abcd" + "efg")
```

`Out`: abcdefg

```python
print("Best", "python", "book" + ":", "This book")
```

`Out`: Best python book: This book

```python
x = 10
print(x)
```

`Out`: 10

```python
name = "James"
ID_num = 789
print("Name:", name + ",", "ID Number:", ID_num)
```

`Out`: Name: James, ID Number: 789



```python
print("James is my friend.\nHe is Korean.")
```

`Out`: James is my friend. 

​		  He is Korean.

※ 개행문자: `\n` 를 추가하면 문자열에서 **줄 바꿈 수행.** 만약에 `\n` 를 두개 입력하면 줄 바꿈 두번 수행됨.



```python
print("Welcome to")
print("python!!")
```

`Out`: Welcome to 

​		  python!!

```python
print("Welcome to ", end = "")
print("python!!")
```

`Out`: Welcome to python!!

※ `end = ""` 입력하면 줄 바꿈 없이 연결되어 출력 수행.



*** 형식 지정 출력**

**나머지 연산자(%)를 이용한 형식 및 위치 지정**

나머지 연산자는 print() 함수에서 데이터의 출력 형식과 위치를 지정할 때도 사용.

```python
print("%type" % data)
```









```python
ani_0 = 'cat'
ani_1 = 'fox'
ani_2 = 'dog'
ani_3 = 'cow'

print("animal: {0},{3}".format(ani_0,ani_1,ani_2, ani_3))
```









#### 02 키보드 입력





#### 03 파일 읽고 쓰기

*** 파일 열기**

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



*** 파일 쓰기**

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



*** 파일 읽기**

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

*** 파일에 문자열 한 줄씩 쓰기**

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

*** 파일에서 문자열 한 줄씩 읽기**

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

*** with 문의 구조**

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



*** with 문의 활용**

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



## 07 함수

> 코딩하다 보면 특정 기능을 반복해서 수행해야 할 때가 있음. 그때 마다 같은 기능을 수행하는 코드를 반복해서 작성하는 것은 비효율적임. 이때 사용할 수 있는 것이 **함수(function)**. 함수는 **특정 기능을 수행하는 코드의 묶음**. 함수를 이용하면 같은 기능을 숭행하는 코드를 반복해서 작성할 필요가 없음. **또한 코드가 깔끔해지고 한번 만든 코드를 재사용할 수 있어서 코드를 작성하기가 편해짐**.

#### 01 함수의 정의와 호출

수학에서 말하는 함수: `y = f(x)`

프로그래밍에서 말하는 함수: 입력값(x, 인자)을 넣으면 연산 후 결과값(y, 반환 값) 출력

*** 함수의 기본 구조**

프로그래밍에서의 함수도 수학의 함수와 유사. 특정 기능을 수행하는 코드의 묶음. **수학 함수에서 입력 값**을 **프로그래밍 함수에서 인자**라고 함. 프로그래밍에서는 인자를 통해 함수에 값을 전달할 수 있음. **수학 함수에서 계산된 결괏값**을 **프로그래밍 함수에서 반환 값**이라고 함. 단, 프로그래밍 함수에서는 수학 함수와 달리 인자와 반환 값이 없을 수도 있음.

```python
def 함수명([인자1, 인자2, ... , 인자n]):
    <코드 블록>
    [return <반환 값>]
```

함수를 호출 할때는 함수를 정의할 때 지정했던 인자 값도 함께 써야 함.

```python
함수명([인자1, 인자2, ... , 인자n]):
```



*** 인자도 반환 값도 없는 함수**

```python
def my_func():
    print("My first function!")
    print("This is a function.")
my_func()
```

`Out`: My first function!
		  This is a function.

*** 인자는 있으나 반환 값이 없는 함수**

```python
def my_friend(friendName):
    print("{}는 나의 친구입니다.".format(friendName))

my_friend("철수")
my_friend("영미")
```

`Out`: 철수는 나의 친구입니다.

​		  영미는 나의 친구입니다.



```python
def my_student_info(name, school_ID, phoneNumber):
    print("----------------------")
    print("- 학생이름:", name)
    print("- 학급번호:", school_ID)
    print("- 전화번호:", phoneNumber)

my_student_info('현아', "01", '01-235-6789')
my_student_info('진수', "02", '01-987-6543')
```

`Out`: <img src="C:\myPyCode\Png file\06-01-01.png" style="zoom:33%;" />



```python
def my_student_info(name, school_ID, phoneNumber):
    print("************************")
    print("* 학생이름:", name)
    print("* 학급번호:", school_ID)
    print("* 전화번호:", phoneNumber)

my_student_info('현아', "01", '01-235-6789')
my_student_info('진수', "02", '01-987-6543')
```

`Out`: <img src="C:\myPyCode\Png file\06-01-02.png" style="zoom: 33%;" />



*** 인자도 있고 반한 값도 있는 함수**

```python
def my_calc(x, y):
    z = x*y
    return z

my_calc(3, 4)
```

`Out`: 12



```python
def my_student_info_list(student_info):
    print("************************")
    print("* 학생이름:", student_info[0])
    print("* 학급번호:", student_info[1])
    print("* 전화번호:", student_info[2])
    print("************************")
    
student1_info = ['현아', "01", '01-235-6789']
my_student_info_list(student1_info)
my_student_info_list(['진수', "02", '01-987-6543'])
```

`Out`: <img src="C:\myPyCode\PNG file\06-01-03.png" style="zoom: 33%;" />



#### 02 변수의 유효 범위

> 함수 안에서 정의한(혹은 생성한) 변수는 함수 안에서만 사용할 수 있음. 함수 안에서 생성한 변수는 함수를 호출해 실행되는 동안만 사용할 수 있고 함수 실행이 끝나면 더는 사용할 수 없음.

**지역 변수(local variable)**

함수 안에서 정의한 변수는 함수 영역 안에서만 동작하는 변수이므로 지역 변수(local variable)라고 함. 지역 변수는 함수가 호출될 때 임시 저장 공간(메모리)에 할당되고 함수 실행이 끝나면 사라짐. 다른 함수에서 같은 이름으로 변수를 사용해도 각각 다른 임시 저장 공 간에 할당되므로 독립적으로 동작.

**전역 변수 (global variable)**

지역 변수의 상대적인 개념으로 함수 밖에서 생성한 변수를 전역 변수 (global variable)라고 함. 지역 변수는 함수 안에서만 사용할 수 있지만 전역 변수는 코드 내 어디서나 사용할 수 있음.

**이름 공간과 변수의 유효 범위**

변수를 정의할 때 변수가 저장되는 공간을 이름 공간이라고 하는데 변수를 함수 안에서 정의했느냐, 함수 밖에서 정의했느냐에 따라 코드 내에 서 영향을 미치는 유효 범위(scope)가 달라짐. 지역 변수를 저장하는 이름 공간을 **지역 영역(local scope)**이라고 하고 전역 변수를 저장하는 이름 공간을 **전역 영역(global scope)**이라고 함. 파이썬 자체에서 정의한 이름 공간을 **내장 영역(built-in scope)**이라고 함.

함수에서 어떤 변수를 호출하면 지역 영역, 전역 영역, 내장 영역 순서대로 변수가 있는지 확인(스코핑 룰(Scoping rule) 혹은 LGB 룰 (Local/Global/Built_in rule) 이라고 함.

함수를 작성할 때 지역 변수와 전역 변수의 이름이 다르다면 문제가 되 지 않지만 만약 동일한 변수명을 지역 변수와 전역 변수에 모두 이용했다면 이것 을 이용할 때 스코핑 룰(Scoping rule) 에 따라 변수가 선택.



```python
a = 5                                # 전역 변수

def func1():
  a = 1                              # 지역 변수. func1() 에서만 사용
  print("[func1] 지역 변수 a =", a)

def func2():
  a = 2                              # 지역 변수. func2() 에서만 사용
  print("[func2] 지역 변수 a =", a)

def func3():  
  print("[func3] 지역 변수 a =", a)  

def func4():
  global a                          # 함수 내에서 전역 변수를 변경하기 위해 선언
  a = 4                             # 전역 변수의 값 변경
  print("[func4] 전역 변수 a =", a)


func1()
func2()
print("전역변수 a =", a)           # 전역 변수 출력
func3()
func4()
func3()
```

`Out`: [func1] 지역 변수 a = 1 

​		  [func2] 지역 변수 a = 2 

​		  전역변수 a = 5 

​		  [func3] 지역 변수 a = 5 

​		  [func4] 전역 변수 a = 4 

​		  [func3] 지역 변수 a = 4



#### 03 람다(lambda) 함수

>  파이썬에는 한 줄로 함수를 표현하는 람다(lambda) 함수가 있음. 람다 함수는 구성이 단순해 간단한 연산을 하는 데 종종 사용됨.

람다 함수의 기본 구조.

```python
lambda <인자> : <인자 활용 수행 코드>
(lambda <인자> : <인자 활용 수행 코드>)(<인자>)  # 실제 사용시 구조

lambda_function = lambda <인자> : <인자 활용 수행 코드>   # 변수로 할당하여 사용
lanbda_functtion(<인자>)
```



```python
(lambda X : X**2) (3)
```

`Out`: 9

```python
mySquare = lambda x : x**2
mySquare(2)
mySquare(5)
```

`Out`: 4

​		  25

```python
mySimpleFunc = lambda x, y, z : 2*x + 3*y +z
mySimpleFunc(1, 2, 3)
```

`Out`: 11



#### 04 유용한 내장 함수

> 코드를 작성하다 보면 데이터의 형태(타입)를 변환해야 하는 경우가 있음. 파이썬의 내장 함수를 이용해 데이터의 형태를 변환할 수 있음.

*** 형 변환 함수**

**정수형으로 변환**

내장 함수 int()는 실수나 문자열(정수 표시) 데이터를 정수로 변환. 실수 데이터를 정수로 변환. 실수의 경우 소수점 이하는 버리는 방식으로 정수로 변환.

```python
[int(0.123), int(3.5123456), int(-1.312367)]
```

`Out`: [0, 3, -1]

```python
[int('1234'), int('5678'), int('-9012')]
```

`Out`: [1234, 5678, -9012]



**실수형으로 변환**

float()는 정수나 문자열(정수 및 실수 표시) 데이터를 실수로 변환. 정수 데이터를 실수로 변환. 실수를 표시한 문자열을 실수로 변환. 문자열에 정수나 실수를 표시하는 문자 외 의 다른 문자가 있으면 float()로 변환할 때 오류가 발생.

```python
[float(0), float(123), float(-567)]
```

`Out`: [0.0, 123.0, -567.0]

```python
[float('10'), float('0.123'), float('-567.89')]
```

`Out`: [10.0, 0.123, -567.89]



**문자형으로 변환**

내장 함수 str()은 정수나 실수 데이터를 문자열로 변환. 정수 데이터를 문자열 데이터로 변환. 실수 데이터를 문자열 데이터로 변환.

```python
[str(123), str(459678), str(-987)]
```

`Out`: ['123', '459678', '-987']

```python
[str(0.123), str(345.678), str(-5.987)]
```

`Out`: ['0.123', '345.678', '-5.987']



**리스트, 튜플, 세트형으로 변환**

| 내장함수 | 기능                             | 사용예                             |
| -------- | -------------------------------- | ---------------------------------- |
| list()   | 튜플/세트 데이터를 리스트로 변환 | list((1, 2, 3)), list({1, 2, 3})   |
| tuple()  | 리스트/세트 데이터를 튜플로 전환 | tuple([1, 2, 3]), tuple({1, 2, 3}) |
| set()    | 리스트/튜플 데이터를 세트로 변환 | set([1, 2, 3]), set((1, 2, 3))     |

※ list == [ ], tuple == ( ), set == { }

```python
list_data = ['abc', 1, 2, 'def']
tuple_data = ('abc', 1, 2, 'def')
set_data = {'abc', 1, 2, 'def'}

[type(list_data), type(tuple_data), type(set_data)]
print("리스트로 변환", list(tuple_data), list(set_data))
print("튜플로 변환", tuple(list_data), tuple(set_data))
print("세트로 변환",set(list_data), set(tuple_data))
```

`Out`: [list, tuple, set]

​		  리스트로 변환 ['abc', 1, 2, 'def'] [1, 2, 'abc', 'def'] 

​		  튜플로 변환 ('abc', 1, 2, 'def') (1, 2, 'abc', 'def') 

​		  세트로 변환 {1, 2, 'abc', 'def'} {1, 2, 'abc', 'def'}



*** bool 함수**

**숫자를 인자로 bool 함수 호출**

내장 함수 bool()은 True 혹은 False의 결과를 반환. bool 함수의 인자가 숫자인 경우 숫자 0이면 False, 0 이외의 숫자 <양의 정수, 음의 정수, 양의 실수, 음의 실수> 이면 True를 반환.

숫자 0을 인자로 삼아 bool() 함수를 호출하면 False를 반환

```python
bool(0)    # 인자: 숫자 0
```

`Out`: False

0 이외의 숫자를 인자로 삼아 bool()함수를 호출하면 모두 True

```python
bool(1)    # 인자: 양의 정수
```

`Out`: True

```python
bool(-10)    # 인자: 음의 정수
```

`Out`: True

```python
bool(5.12)    # 인자: 양의 실수
```

`Out`: True

```python
bool(-3.26)    # 인자: 음의 실수
```

`Out`: True



**문자열을 인자로 bool 함수 호출**

bool() 함수의 인자가 문자열인 경우 문자열이 있으면 True를 반환하 고 없으면 False를 반환. **bool()함수를 어떤 문자열이 빈 문자열인지 아닌지를 검사하는 데 이 용할 수 있음.** 문자열에서 공백은 공백 문자열이 있는 것이고 빈 문자열('')은 문자 열이 없는 것. 파이썬에서 None 은 아무것도 없는 것으로 간주.

 함수 bool()의 인자로 문자열을 사용예

```python
bool('a')     # 인자: 문자열 'a'
```

`Out`: True

```python
bool(' ')     # 인자: 빈 문자열(공백)
```

`Out`: True

```python
bool('')      # 인자: 문자열 없음
```

`Out`: False

```python
bool(None)    # 인자: None
```

`Out`: False



**▶ 깜짝 함수 만들기 퀴즈**

```python
# 함수정의
# 입력: 이름
# 처리: 
# 1. 이름 있으면 출력 --> '입력된 이름: <입력된 이름>'
# 2. 이름이 없으면 '이름이 없습니다.' 출력
# 처리 값 출력.

def name_print():
  a = input('이름을 쓰시오')
  if bool(a) == True:
    print('입력된 이름:', a)
  else:
    print('입력된 이름이 없습니다.')
name_print()
```



**리스트, 튜플, 세트를 인자로 bool 함수 호출**

리스트, 튜플, 세트를 인자로 bool 함수 호출. bool()함수는 리스트, 튜플, 세트를 인자로 호출할 수도 있음. 문자열과 마찬가지로 항목이 있으면 True, 없으면 False를 반환. **bool() 함수는 리스트, 튜플, 세트 데이터에서 항목이 있는지 없는지 검사할 때 유용하게 이용할 수 있음.**

```python
myFriends = []
bool(myFriends)    # 인자: 항목이 없는 빈 리스트
```

`Out`: False

```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
bool(myFriends)    # 인자: 항목이 있는 빈 리스트
```

`Out`: True

```python
myNum = ()
bool(myNum)        # 인자: 항목이 없는 빈 튜플
```

`Out`: False

```python
myNum = (1, 2, 3)
bool(myNum)        # 인자: 항목이 있는 빈 튜플
```

`Out`: True

```python
mySetA = {}
bool(mySetA)       # 인자: 항목이 없는 빈 세트
```

`Out`: False

```python
mySetA = {1, 2, 3}
bool(mySetA)       # 인자: 항목이 있는 빈 세트
```

`Out`: True



**bool 함수의 활용**

```python
def print_name(name):
    if bool(name):
        print('입력된 이름:', name)
    else:
        print('입력된 이름이 없습니다.')
```

`print_name('James')`

`Out`: 입력된 이름: James

`print_name('')`

`Out`: 입력된 이름이 없습니다. 



*** 최솟값과 최댓값을 구하는 함수**

데이터에서 최소값 혹은 최대값을 구할 때 내장 함수 min()과 max()를 이용. 내장 함수 min()과 max()는 리스트, 튜플, 세트의 항목이나 문자열 중에 서 각각 최소값과 최대값을 반환. 

숫자를 포함한 리스트에서 최소값과 최대값을 구하기.

```python
myNum = [10, 5, 12, 0, 3.5, 99.5, 42]
[min(myNum), max(myNum)]
```

`Out`: [0, 99.5]

숫자 뿐만 아니라 문자열에 대해서도 최소값과 최대값을 구할 수 있음.

문자열을 입력해 문자열에서 최소값과 최대값을 구하기.

```python
myStr = 'zxyabc'
[min(myStr), max(myStr)]
```

`Out`: ['a', 'z']

각각 튜플과 세트에서 최소값과 최대값을 구하기

```python
myNum = (10, 5, 12, 0, 3.5, 99.5, 42)
[min(myNum), max(myNum)]
```

`Out`: [0, 99.5]

```
myNum = {'Abc', 'abc', 'bcd', 'efg'}
[min(myNum), max(myNum)]
```

`Out`: ['Abc', 'efg']

※ 크기를 비교하고자 하는 항목이 문자열일 경우에는 첫 문자 먼저 비교하고, 첫 문자가 같다면 두 번째 문자를 비교하는 식으로 전체를 비교함. **로마자 알파벳의 경우 A ~ Z, a ~ z 순서대로 크기가 큼**. 문자열로 된 **숫자와 로마자 알파벳을 비교했을 때 숫자가 더 작음**.



*** 절대값과 전체 합을 구하는 함수**

절대값은 숫자의 부호와 상관없이 숫자의 크기만을 나타냄. 내장 함수 abs()로 숫자의 절대값을 구할 수 있음.

 abs()를 이용해 숫자의 절대값을 구하기

```python
[abs(10), abs(-10)]
```

`Out`: [10, 10]

```python
[abs(2.45), abs(-2.45)]
```

`Out`: [2.45, 2.45]

내장 함수 sum()은 리스트, 튜플, 세트 데이터의 모든 항목을 더해 전체 합을 결과값으로 반환. sum()을 이용해 리스트 데이터의 모든 항목을 더하기. 튜플과 세트 데이터에 대해서도 sum() 함수를 적용해 모든 항목의 합을 구할 수 있음.

```
sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum(sumList)
```

`Out`: 55



*** 항목의 개수를 구하는 함수**

문자열, 리스트, 튜플, 딕셔너리 안에 있는 항목의 개수를 알아야 할 때 **내장 함수 len()은 항목의 개수(데이터의 길이)를 반환**. len()으로 문자열, 리스트, 튜플, 딕셔너리 데이터의 길이를 구하기

```python
len('ab cd')                              # 문자열
```

`Out`: 5

```python
len([1, 2, 3, 4, 5, 6, 7, 8])             # 리스트
```

`Out`: 8

```python
len((1, 2, 3, 4, 5))                      # 튜플
```

`Out`: 5

```python
len({'a', 'b', 'c', 'd'})                 # 세트
```

`Out`: 4

```python
len({1:'Thomas', 2:'Edward', 3:'Henry'})  # 딕셔너리
```

`Out`: 3

※ 문자열은 공백을 포함한 문자 길이(개수)를 구할 수 있고 리스트, 튜플, 딕셔너리는 항목의 길이(개수)를 구할 수 있음.



*** 내장 함수의 활용**

시험 점수가 입력된 리스트가 있다고 할 때 sum()과 len()을 이용해 데이터 항목의 총합과 길이를 구할 수 있음. 이를 이용하면 평균값도 쉽게 구할 수 있음.

내장함수 `sum()`과 `len()`을 사용하지 않고 총점과 평균값 구하기

```python
scores = [90, 80, 95, 85]                     # 과목별 시험 점수

score_sum = 0                                 # 총점 계산을 위한 초깃값 설정
subject_nm = 0                                # 과목수 계산을 위한 초깃값 설정
for score in scores:
    score_sum = score_sum + score             # 과목별 점수 모두 더하기
    subject_num = subject_num + 1             # 과목수 계산
    
average = score_sum / subject_num             # 평균(총점 / 과목수) 구하기

print('총점:{0}, 평균: {1}'.format(score_sum, average))
```

`Out`: 총점: 350, 평균: 87.5



내장함수 `sum()`과 `len()`을 사용하여 총점과 평균값 구하기

```python
scores = [90, 80, 95, 85]                     # 과목별 시험 점수
print('총점:{0}, 평균: {1}'.format(sum(scores), sum(scores)/len(scores)))
```

`Out`: 총점: 350, 평균: 87.5

```python
print('최하점수:{0}, 최고점수: {1}'.format(min(scores), max(scores)))
```

`Out`: 최하점수: 80, 최고점수: 95



## 08 객체와 클래스







## 09 문자열과 텍스트 파일 데이터 다루기

> 데이터가 포함된 텍스트 파일에서 문자 열을 읽어올 수 있어야 함. 사용목적에 맞게 문자열을 처리할 수 있어야 함. 파이썬에서는 문자열 처리를 위한 다양한 내장 문자열 메서드가 제공 되므로 문자열을 처리하기 쉬움. 

#### 01 문자열 다루기

파이썬에서는 큰따옴표(")나 작은따옴표(') 안에 들어 있는 문자의 집합을 문자열 이라고 함. 한 텍스트 파일의 내용을 읽어 오면 그것도 문자열임. 텍스트 파일을 읽어서 가져온 문자열은 대부분 문자열 처리를 통해 원하는 형태의 데이터로 변환해서 이용. 문자열을 처리하기 위해서 는 문자열 분리, 불필요한 문자열 제거,  문자열 연결 등을 할 수 있어야 함.

*** 문자열 분리하기**

문자열을 부분 문자열로 나누고 싶을 때는 split() 메서드를 이용.

```python
str.split([sep])
```

split() 메서드는 문자열(str)에서 구분자(separator)인 sep을 기준으로 문자 열을 분리해 리스트로 반환. 소괄호 안의 대괄호([ ]) 부분은 생략할 수 있음. 구분자(sep)를 입력하지 않고 str.split()을 수행하면 문자열 사이의 모든 공 백과 개행문자(\n)를 없애고 분리된 문자열을 항목으로 담은 리스트를 반환.

콤마(,)로 구분된 단어가 여러 개 적힌 문자열이 있을 때 구분자를 콤마(,) 로 입력해 split() 메서드를 적용하면 콤마를 기준으로 단어를 분리.

```python
coffee_menu_str = "에스프레소, 아메리카노, 카페라테, 카푸치노"
coffee_menu_str.split(',')
```

`Out`: ['에스프레소', ' 아메리카노', ' 카페라테', ' 카푸치노']



문자열에 직접 split() 메서드 사용 가능.

```python
"에스프레소, 아메리카노, 카페라테, 카푸치노".split(',')
```

`Out`: ['에스프레소', ' 아메리카노', ' 카페라테', ' 카푸치노']



공백으로 구분된 문자열에 인자 없이 split() 메서드 사용 가능.

```python
"에스프레소 아메리카노 카페라테 카푸치노".split()
```

`Out`: ['에스프레소', ' 아메리카노', ' 카페라테', ' 카푸치노']



문자열에 인자 없이 split()를 사용하면 문자열 사이의 모든 공백과 개행 문자(\n)를 없애고 분리된 문자열을 반환. 단어 사이에 공백과 개행문자가 아무리 많더라도 split() 이용하면 공백과 개행문자를 모두 없애고 문자열을 분리.

```python
"  에스프레소  \n\n  아메리카노  \n  카페라테     카푸치노 \n".split()
```

`Out`: ['에스프레소', ' 아메리카노', ' 카페라테', ' 카푸치노']



문자열을 분리할 때 인자 maxsplit을 추가하면 앞에서부터 원하는 횟수 만큼만 문자열을 분리 할 수 있음.

```python
str.split([sep ,] maxsplit = 숫자)
```

문자열(str)을 구분자 sep(생략 가능)을 기준으로 maxsplit만큼 분리해 리스트로 반환.

```python
"에스프레소 아메리카노 카페라테 카푸치노".split(maxsplit = 2)
```

`Out`: ['에스프레소', '아메리카노', '카페라테 카푸치노']

인자로 지정한 maxSplit=2로 인해 앞에서부터 2개의 공백(sep)까지만 문자열을 나눠 결과적으로 3개의 항목이 담긴 리스트를 반환.



```python
phone_number = "+82-01-2345-6789"            # 국가 번호가 포함된 전화번호
split_num = phone_number.split("-", 1)       # 국가 번호와 나머지 번호 분리

print(split_num)
print("국내전화번호: {0}".format(split_num[1]))
```

`Out`: ['+82', '01-2345-6789']

​		  국내전화번호: 01-2345-6789



*** 필요없는 문자열 삭제하기**

문자열에서는 앞뒤 공백 혹은 개행문자와 같이 불필요한 부분을 지워야 할 때 사용할 수 있는 것이 strip() 메서드.

```python
str.strip([chars])
```

strip()메서드는 문자열(str)의 앞과 뒤에서 시작해서 지정한 문자(chars)  외의 다른 문자를 만날 때까지 지정한 문자(chars)를 모두 삭제한 문자 열을 반환. 지정한 문자(chars)와 일치하는 것이 없으면 문자열(str)을 그대로 반환. 지정한 문자(chars)가 여러 개일 경우 순서는 상관이 없음. 지정한 문자(chars) 없이 str.strip()를 수행하면 문자열 앞과 뒤의 모든 공백과 개행문자(\n)를 삭제한 후에 문자열을 반환.

```python
str = "    Python    "
str.strip()                     # 공백과 줄 바꿈 제거
```

`Out`: Python

```python
"aaaaaaaaPythonaaaaa".strip('a')
```

`Out`: Python

```python
test_str = "aaaabbPythonbbbaaaaa"
temp1 = test_str.strip('a')        # 문자열 앞뒤의 'a' 제거
temp1
temp1.strip('b')
```

`Out`: bbPythonbbb

```python
test_str = "aaaabbPythonbbbaaaaa"
temp1 = test_str.strip('a')        # 문자열 앞뒤의 'a' 제거
temp1.strip('b')                   # 문자열 앞뒤위 'b' 제거
```

`Out`: Python



strip()메서드의 경우에는 제거하고자 하는 문자를 하나만 지정해서 여러 번 수행 할 수도 있지만 지우고자 하는 문자를 모두 지정해서 한 번에 제거할 수도 있음. 지우고자 하는 문자를 여러 개 지정할 때 순서는 상관이 없음. 지우고자 하는 문자의 순서를 바꿔서 지정해도 됨.

```python
test_str = "aaaabbPythonbbbaaaaa"
test_str.strip('ab')
```

`Out`: Python

```python
test_str = "aaaabbPythonbbbaaaaa"
test_str.strip('ba')
```

`Out`: Python

```python
test_str_multi = "##***!!## ... Python is powerful..!!.!..!! %**##..%%  "
test_str_multi.strip('! # % * .')           # 순서 변경해도 동일한 결과 나옮.
```

`Out`: Python is powerful

```python
"    Python    ".strip(' ')              # 공백 제거
```

`Out`: Python

```python
" \n   Python \n  \n \n".strip(' \n')     # 공백과 줄 바꿈 같이 제거
```

`Out`: Python



strip()메서드는 문자열(str)의 앞과 뒤에서 시작해서 지정한 문자(chars)  외의 다른 문자를 만날 때까지만 지정한 문자(chars)를 삭제. 따라서 `'aaaaballaaaa'` 같은 문자열에 `.strip('a')`를 수행하면 'ball'의 'a'는 지워지지 않음.

```python
"aaaaaaaBallaaaaaa".strip('a')
```

`Out`: Ball



문자열의 앞뒤 공백과 개행문자는 모두 삭제되지만 문자열 사이에 있는 공백과 개행문자는 삭제되지 않음.

```python
"\n This is very \n fast \n\n".strip()
```

`Out`: This is very \n fast



앞이나 뒤 중에서 한쪽만 삭제하고 싶으면 lstrip()나 rstrip() 메서드를 사용. 문자열 왼쪽 (즉,앞쪽) 부분만 삭제하려면 Istrip()메서드. 문자열 오른쪽 (즉,뒤쪽) 부분만 삭제하려면 rstrip()메서드를 이용.

```python
str_lr = "000Python is easy to learn.000"
print(str_lr.strip('0'))
print(str_lr.lstrip('0'))
print(str_lr.rstrip('0'))
```

`Out`: Python is easy to learn. 

​		  Python is easy to learn.000 

​		  000Python is easy to learn.



콤마와 공백을 포함한 문자열에서 콤마를 기준으로 문자열을 분리하고 공백을 모두 제거. coffee_menu 변수에는 콤마와 공백을 포함한 여러 커피 종류가 있음. split(',')을 이용해 콤마를 구분자로 삼아 문자열을 리스트로 분리.

```python
coffee_menu = "  에스프레소, 아메리카노,    카페라테    , 카푸치노 "
coffee_menu_list = coffee_menu.split(',')
coffee_menu_list
```

`Out`: ['  에스프레소', ' 아메리카노', '    카페라테    ', ' 카푸치노 ']








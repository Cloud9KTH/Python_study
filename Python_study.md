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

print() 함수의 인자에는 두 개의 %가 있음. 첫 번째는 따옴표로 둘러싼 문자열 '%type’에서 사용했고 두 번째는 **'% data'**에서 사용. 따옴표와 **'% data' 사이에 콤마가 없고 공백이 있다는 점에 유의**. '%type'은 data 형식에 따라 다른 값을 지정.  data가 문자열이면 %s를, 정수이면 %d(혹은 %i)룰, 실수이면 %f(혹은 %F)룰 지정.  실수의 경우 %f로 표시 하면 기본적으로 소수점 6자리까지 출력.

 data가 두 개 이상이면 따옴표로 둘러싼 문자열 안에 data의 개수에 맞게 '%type'를 순서대로 입 력하고 튜플 형식으로 data를 묶어서 이용. print() 함수에서 data가 두 개일 때 나머지 연산자를 이용해 data를 출력 하는 형식과 위치를 지정하는 구조.

```python
 print("%type %type" % (datal, data2))
```



```python
name = "광재"
print("%s는 나의 친구 입니다." % name)
```

`Out`: 광재는 나의 친구 입니다.



```python
r = 3                                      # 변수 r에 정수 데이터 할당
PI = 3.1415926535879                       # 변수 PI에 실수 데이터 할당
print('반지름: %d, 원주율: %f' %(r, PI))   # 지정된 위치에 데이터 출력
```

`Out`: 반지름: 3, 원주율: 3.141593



**형식 지정 문자열에서 출력 위치 지정**

```python
print("{0} {1} {2} ... {n}".format(data_0, data_1, data_2, ... , data_n))
```

{N}의 N은 0부터 시작하는 숫자로 format()에서 데이터의 위치(0부터 시작)를 의미. {N}에는 format()에서 N에 해당하는 위치의 데이터가 들어가서 출력. {0}에는 data_0가 출력되고 {1}에는 data_1이 출력하고 {n}에는 data_n이 출력.



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

#### 01 클래스 선언과 객체 생성

*** 객체란?**

객체는 속성(상태, 특징)과 행위(행동, 동작, 기능)로 구성된 대상을 의미. 객체는 자동차나 로봇 같은 사물일 수도 있고 사람이나 동물일 수 있으 며 어떤 개념일 수도 있음. 프로그래밍 언어에서 객체를 만들 때는 주로 현실 세계를 반영. 객체의 특징인 속성은 변수로, 객체가 할 수 있는 일인 행동은 함수로 구현. **객체는 변수와 함수의 묶음.**

사람이라면 이름, 키, 몸무게 같은 속성은 변수로 구현하고 걷거나 뛰거 나 앉는 행동은 함수로 구현. 객체가 자전거라면 바퀴의 크기, 색깔 같은 속성은 변수로 구현하고 전진, 방향 전환, 정지 같은 동작은 함수로 구현. 객체를 만들고 이용할 수 있는 기능을 제공하는 프로그래밍 언어를 객 체지향 프로그래밍(Object- Oriented Programming, OOP) 언어 혹은 객체지향 언어라고 함.

*** 클래스 선언**

객체를 만들려면 먼저 클래스를 선언해야 함. **클래스는 객체의 공통된 속성과 행위를 변수와 함수로 정의한 것**. **클래스는 객체를 만들기 위한 기본 틀**이고 **객체는 기본 틀을 바탕으로 만들어진 결과**. 객체는 클래스에서 생성하므로 객체를 클래스의 인스턴스(Instance)라 고 함.

클래스 선언을 위한 기본 구조.

```python
class 클래스명():
    [변수1] #클래스변수 
    [변수2]
    
    def 함수1(self[, 인자1, 인자2, • • , 인자n]): # 클래스 함수 
        〈코드 블록〉
        
    def 함수2(self[, 인자1, 인자2, • • , 인자n]):
        〈코드 블록〉

```

클래스를 선언할 때 class 키워드 다음에 클래스명, 소괄호，콜론(:)을 순서대로 입력. **클래스명 (클래스 이름)은 보통 로마자 알파벳 대문자로 시작하며** 여러 단어가 연결 된 클래스 이름은 가독성을 위해 대문자로 시작하는 단어를 연결해 클래스 이름을 만듦. 클래스 내에서 변수를 선언하고 `def 함수():` 형태로 함수를 작성. 클래스명 다음 줄에 오는 모든 코드는 들여쓰기 해야 함. **클래스에서 정의한 함수의 첫 번째 인자는 self**. **self는 객체 생성 후에 자신을 참조하는데 이용**. 대괄호([ ]) 안에 있는 인자는 필요한 만큼 사용할 수 있으며, 필요 없으면 생략할 수 있음.



*** 객체 생성 및 활용**

예제로 사용할 클래스는 자전거 클래스. 자전거 클래스를 만들기 전에 우선 자전거가 갖는 속성과 동작을 정의. 

자전거의 속성: 바퀴 크기(wheel_size), 색상(color)

자전거의 동작 지정된 속도로 이동(move), 좌/우회전(turn), 정지(stop)

자전거의 속성과 동작을 바탕으로 자전거 클래스를 만듬. 자전거 클래스를 선언하고 객 체를 생성한 후 클래스에 변수와 함수를 추가해서 클래스를 완성.

자전거 클래스를 선언. 클래스를 단순화하기 위해 클래스명이 Bicycle인 자전거 클래스의 원형 만 선언. 클래스에는 클래스명(Bicycle)만 있고, 코드 부분에는 Pass만 있어서 실제로는 아무 일도 일어나지 않음. Bicycle 클래스에는 변수도 함수도 없지만 이것도 엄연한 클래스.

```python
class Bicycle():   # 클래스 선언
	pass
```

선언된 클래스로부터 클래스의 인스턴스인 객체를 생성하는 방법.

```python
객체명 = 클래스명()
```

클래스명()의 클래스는 앞에서 미리 선언돼 있어야 함. 객체명은 변수명을 만들 때와 같은 규칙을 적용해서 만듬.

정의한 Bicycle 클래스의 객체는 아래와 같이 생성할 수 있음.

```python
my_bicycle = Bicycle()
```

선언한 Bicycle 클래스에는 변수도 없고 함수도 없으므로 아직은 어떤 작업도 수행할 수 없지만 my_bicyde 객체는 Bicycle 클래스의 인스턴스임. 객체를 실행하면 객체의 클래스와 객체를 생성할 때 할당받은 메모리의 주소값을 출력함.

```python
my_bicycle
```

```
Out:
<__main__.Bicycle at 0x7fd881bcbad0>
```



 객체에 속성을 설정하려면 '객체명.변수명'에 '속성값’을 할당.

```
객체명.변수명 = 속성값
```

```python
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'
```

객체의 변수에 접근해서 객체의 속성을 가져오는 방법.

```
객체명.변수명
```

객체의 속성값을 가져와서 출력.

```python
print('바퀴 크기:', my_bicycle.wheel_size)
print('색상:', my_bicycle.color)
```

```
Out:
바퀴 크기: 26
색상: black
```









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



콤마와 공백을 포함한 문자열에서 콤마를 기준으로 문자열을 분리하고 공백을 모두 제거. coffee_menu 변수에는 콤마와 공백을 포함한 여러 커피 종류가 있음. **split(',')을 이용해 콤마를 구분자로 삼아 문자열을 리스트로 분리.**

```python
coffee_menu = "  에스프레소, 아메리카노,    카페라테    , 카푸치노 "
coffee_menu_list = coffee_menu.split(',')
coffee_menu_list
```

`Out`: ['  에스프레소', ' 아메리카노', '    카페라테    ', ' 카푸치노 ']

 coffee_menu_list에는 공백을 포함한 문자열을 항목으로 갖는 리스트 가 반환. 리스트 변수 coffee_menu_list의 모든 항목에 공백을 제거하기 위해 항목마다 strip() 메서드를 적용. 공백이 제거된 문자열은 append()를 이용해 리스트 변수 coffee_list에 하나씩 추가하면 최종적으로 원하는 결과를 얻을 수 있음.

```python
coffee_list = []                            # 빈 리스트 생성
for coffee in coffee_menu_list:
    temp = coffee.strip()                   # 문자열의 공백 제거
    coffee_list.append(temp)                # 리스트 변수에 공백이 제거된 문자열 추가

print(coffee_list)                          # 최종 문자열 리스트 출력
```

`Out`: ['에스프레소', '아메리카노', '카페라테', '카푸치노']



*** 문자열 연결하기**

```python
name1 = '철수'
name2 = '영희'
hello = '님, 주소와 전화 번호를 입력해 주세요.'

print(name1 + hello)
print(name2 + hello)
```

`Out`: 철수님, 주소와 전화 번호를 입력해 주세요. 

​		  영희님, 주소와 전화 번호를 입력해 주세요.



문자열이 아니라 리스트의 모든 항목을 하나의 문자열로 만들려면? 리스트의 모든 항목을 하나의 문자열 join() 메서드를 사용.

```python
str.join(seq)
```

join() 메서드는 문자열을 항목으로 갖는 시퀀스(seq)의 항목 사이에 구분자 문자열(str)을 모두 넣은 후에 문자열로 반환. 시퀀스는 리스트나 튜플과 같이 여러 데이터를 순서대로 담고 있는 나 열형 데이터.  문자열을 항목으로 갖는 문자열 리스트를 join() 메서드를 이용해 문자 열로 변환하는 과정. 문자열 리스트의 항목 사이에는 구분자 문자열(한 칸 공백)이 들어감

```python
address_list = ['서울시', '서초구', '반포대로', '201(반포동)']
address_list
```

`Out`: ['서울시', '서초구', '반포대로', '201(반포동)']

```python
a = ' '
a.join(address_list)
```

`Out`: 서울시 서초구 반포대로 201(반포동)

```python
" ".join(address_list)
```

`Out`: 서울시 서초구 반포대로 201(반포동)

```python
"*^^*".join(address_list)
```

`Out`: <img src="C:\myPyCode\Png file\09-01-01.png" style="zoom:33%;" />



*** 문자열 찾기**

```python
str.find(search_str)
```

find() 메서드는 문자열(str)에서 찾으려는 검색 문자열(search_str)과 첫번째로 일치하는 문자열(str)의 위치를 반환. **문자열의 위치는 0부터 시작**. 문자열에서 검색 문자열을 찾을 수 없으면 -1을 반환.

```python
str_f = "Python code."

print('찾는 문자열의 위치:', str_f.find("Python"))
print('찾는 문자열의 위치:', str_f.find("code"))
print('찾는 문자열의 위치:', str_f.find("n"))
print('찾는 문자열의 위치:', str_f.find("easy"))
```

`Out`: 찾는 문자열의 위치: 0 

​		  찾는 문자열의 위치: 7 

​		  찾는 문자열의 위치: 5 

​		  찾는 문자열의 위치: -1



str.find(search_str)에 시작 위치(start)와 끝 위치(end)를 추가로 지정 해서 검색 범위를 설정할 수도 있음.

```python
 str.find(search_str, start, end)
```

start ~ end-1 범위에서 검색 문자열(search_str)을 검색해 일치하는 문자열(str)의 위치를 반환. 지정된 범위에서 찾지 못하면 -1 을 반환.



시작 위치만 지정해서 검색 범위를 설정할 수도 있음. 

```python
str.find(search_str, start)
```

검색 범위는 start부터 문자열(str)의 끝이 됨.



```python
str_f_se = 'Python is powerful. Pyton is easy to learn.'

print(str_f_se.find("Python", 10, 30))     # 시작 위치(start)와 끝 위치(end) 지정
print(str_f_se.find("Python", 35))         # 찾기 위한 시작 위치(start) 지정
```

`Out`: 20

​		  -1



해당 문자열이 몇 번 나오는지 알고 싶다면 **count() 메서드를 이용.**

```python
str.count(search_str)
str.count(search_str, start)
str.count(search_str, start, end)
```

count()메서드는 문자열(str) 에서 찾고자 하는 문자열(search_str)과 일치하는 횟수를 반환하고, 없으면 0을 반환. find()와 마찬가지로 start와 end로 검색 범위를 지정할 수도 있음.

```python
str_c = "Python is powerful. Python is easy to learn. Python is open"

print('Python의 개수는?:', str_c.count('Python'))
print('powerful의 개수는?:', str_c.count('powerful'))
print('IPython의 개수는?:', str_c.count('IPython'))
```

`Out`: Python의 개수는?: 3 

​		  powerful의 개수는?: 1 

​		  IPython의 개수는?: 0



다른 찾기 메서드로 **startwith() 메서드**와 **entwith() 메서드**가 있음. 각각 문자열이 지정된 문자 열로 시작하는지 끝나는지를 검사할 때 사용.

```python
str.startswith(prefix)
str.startswith(prefix, start)
str.startswith(prefix, start, end)
```

 startswith() 메서드는 문자열(str)이 지정된 문자열(prefix)로 시작되면 True, 그렇지 않으면 False를 반환. find()와 마찬가지로 start와 end로 범위를 지정할 수도 있음.



```python
str.endswith(suffix)
str.endswith(suffix, start)
str.endswith(suffix, start, end)
```

endswith()메서드는 문자열(str)이 지정된 문자열(suffix)로 끝나면 True, 그렇지 않으면 False를 반환. start와 end로 범위를 지정할 수도 있음.



```python
str_se = "Python is powerful. Python is easy to learn."

print("Python으로 시작?:", str_se.startswith("Python") )
print("is로 시작?:", str_se.startswith("is") )
print(".로 끝?:", str_se.endswith(".") )
print("learn으로 시작?:", str_se.endswith("learn") )
```

`Out`: Python으로 시작?: True 

​		  is로 시작?: False 

​		  .로 끝?: True 

​		  learn으로 시작?: False



*** 문자열 바꾸기**

```python
str.replace(old, new[, count])
```

replace() 메서드는 문자열(str)에서 지정한 문자열(old)을 찾아서 새로 운 문자열(new)로 바꿈. count는 문자열(str)에서 지정된 문자열을 찾아서 바꾸는 횟수. 횟수를 지정하지 않으면 문자열 전체에서 찾아서 바꿈.

```python
str_a = 'Python is fast. Python is friendly. Python is open.'
print(str_a.replace('Python','IPython'))
print(str_a.replace('Python','IPython', 2))
```

`Out`: IPython is fast. IPython is friendly. IPython is open. 

​		  IPython is fast. IPython is friendly. Python is open.



특정 문자열을 삭제할 때도 replace() 메서드를 이용할 수 있음. 문자열에서 ‘['와 ']’를 제거. **replace() 메서드에는 문자열을 하나씩만 지정할 수 있으므로** ‘[’와 ’]’를 모두 제거하려면 replace() 메서드를 두 번 사용.

```python
str_b = '[Python] [is] [fast]'
str_b1 = str_b.replace('[', '')     # 문자열에서 '['를 제거
str_b2 = str_b1.replace(']', '')    # 결과 문자열에서 다시 ']'를 제거

print(str_b)
print(str_b1)
print(str_b2)
```

`Out`: [Python] [is] [fast] 

​		  Python] is] fast] 

​		  Python is fast



*** 문자열의 구성 확인하기**

※ 문자열의 구성을 확인하기 위한 메서드

| 메서드    | 설명                                                         | 사용 예       |
| --------- | ------------------------------------------------------------ | ------------- |
| isalpha() | 문자열이 숫자, 특수 문자, 공백이 아닌 문자로 구성돼 있을 때만 True, 그 밖에는 False 반환 | str.isalpha() |
| isdigit() | 문자열이 모두 숫자로 구성돼 있을 때만 True, 그 밖에는 False 반환 | str.isdigit() |
| isalnum() | 문자열리 특수 문자나 공백이 아닌 문자와 숫자로 구성돼 있을 때만 True, 그 밖에는 False 반환 | str.isalnum() |
| isspace() | 문자열이 모두 공백 문자로 구성돼 있을 때만 True, 그 밖에는 False 반환 | str.isspace() |
| isupper() | 문자열이 모두 로마자 대문자로 구성돼 있을 때만 True, 그 밖에는 False 반환 | str.isupper() |
| islower() | 문자열이 모두 로마자 소무낮로 구성돼 있을 때만 True, 그 밖에는 False 반환 | str.islower() |



```python
print('Python' .isalpha())       # 문자열에 공백, 특수 문자, 숫자가 없음
print('Ver. 3.x' .isalpha())     # 공백, 특수 문자, 숫자 중 하나가 있음
```

`Out`: True

​		  False



```python
print('12345' .isdigit())       # 문자열이 모두 숫자로 구성됨
print('12345abc' .isdigit())    # 문자열이 숫자로만 구성되지 않음
```

`Out`: True

​		  False



```python
print('abc1234' .isalnum())     # 특수 문자나 공백이 아닌 무낮와 숫자로 구성됨
print('   abc1234' .isalnum())  # 문자열에 공백이 있음
```

`Out`: True

​		  False



```python
print('   ' .isspace())         # 문자열이 공백으로만 구성됨
print(' 1 ' .isspace())         # 문자열에 공백 외에 다른 문자가 있음
```

`Out`: True

​		  False



```python
print('PYTHON' .isupper())      # 문자열이 모두 대문자로 구성됨
print('Python' .isupper())      # 문자열에 대문자와 소문자가 있음
print('python' .islower())      # 문자열이 모두 소문자로 구성됨
print('Python' .islower())      # 문자열에 대문자와 소문자가 있음
```

`Out`: True

​		  False

​          True

​		  False



*** 대소문자로 변경하기**

lower() 메서드는 문자열(str)에서 로마자 알파벳의 모든 문자를 소문자 로 바꾸고 upper() 메서드는 대문자로 바꿈.

```python
str.lower()
str.upper()
```



```python
string1 = 'Python is powerful. PYTON IS EASY TO LEARN.'
print(string1.lower())
print(string1.upper())
```

`Out`: python is powerful. pyton is easy to learn. 

​		  PYTHON IS POWERFUL. PYTON IS EASY TO LEARN.

```python
'Python' == 'python'
```

`Out`: False

```python
print('Python' .lower() == 'python' .lower())
print('Python' .upper() == 'python' .upper())
```

`Out`: True

​		  True



#### 02 텍스트 파일의 데이터를 읽고 처리하기

**데이터 파일 준비 및 읽기**

* 데이터: 어느 커피 전문점에서 나흘 동안 기록한 메뉴별 커피 판매량 

* 원하는 직업: 4일 동안 메뉴당 전체 판매량과 하루 평균 판매량 구하기

`coffeShopSales.txt` 라는 파일이 있다고 가정. 윈도우 에서는 `type` 명령어 사용하고 IPython 아니 주피터 노트북에서는 `! 명령어`로 실행. `type` 명령어 쓰면 파일의 내용 출력.

```python
!type coffeeShopSales.txt
```

`Out`: <img src="C:\myPyCode\Png file\09-02-01.png" style="zoom:33%;" />

```python
file_name = 'c:/myPyCode/coffeeShopSales2.txt'

f = open(file_name)           # 파일 열기
for line in f:                # 한 줄씩 읽기
    print(line, end='')       # 한 줄씩 출력
f.close()                     # 파일 닫기
```

`Out`: <img src="C:\myPyCode\Png file\09-02-02.png" style="zoom:33%;" />

파일명을 경로와 함께 지정해 file_name 변수에 할당한 후 파일 열기로 해당 파일을 열고 한 줄씩 읽어서 line 변수에 할당하고 출력. line 변수에는 문자열 한 줄 전체가 들어가 있음.



**파일에서 읽은 문자열 데이터 처리**

첫 번째 줄에 있는 항목 이름을 가져와 빈칸을 기준으로 나누고 두 번째 줄 이후의 항목 값을 처리.  첫 번째 줄의 항목 이름을 가져오는 코드.

```python
f = open(file_name)     # 파일 열기
header = f.readline()   # 데이터의 첫 번째 줄을 읽음
f.close()               # 닫기

header
```

`Out`: 날짜    에스프레소  아메리카노  카페라테  카푸치노\n



줄의 문자열을 분리해 리스트로 변환하려고 하는데 단어 사이에 공백 과 개행문자가 있음. 인자 없이 split() 메서드를 호출해 첫 줄의 문자열 에서 항목 이름을 분리해 리스트로 만듬.

```python
header_list = header.split()   # 첫 줄의 문자열을 분리후 리스트로 변환
header_list
```

`Out`: ['날짜', '에스프레소', '아메리카노', '카페라테', '카푸치노']

 첫번째 줄에 있는 항목 이름을 리스트 변수인 header_list에 할당.



for문을 이용해 두 번째 줄부터 끝줄까지의 데이터를 문자열에서 공백 과 개행문자를 제거하고 각 항목을 data_list에 넣는 코드를 추가.

```python
f = open(file_name)               # 파일 열기
header = f.readline()             # 데이터의 첫 번째 줄을 읽음
header_list = header.split()      # 첫 줄의 문자열을 분리한 후 리스트로 변환

for line in f:                    # 두번째 줄부터 데이터를 읽어서 반복적으로 처리
    data_list = line.split()      # 문자열을 분리해서 리스트로 변환
    print(data_list)              # 결과 확인을 위해 리스트 출력
    
f.close()                         # 파일 닫기
```

`Out`: ['10.15', '10', '50', '45', '20'] 

​		  ['10.16', '12', '45', '41', '18'] 

​		  ['10.17', '11', '53', '32', '25'] 

​		  ['10.18', '15', '49', '38', '22']

출력 결과를 보면 리스트 변수 data_list의 각 항목이 문자열로 되어 있음. 전체 판매량과 평균 을 계산하려면 일일 판매량 데이터 문자열은 숫자 로 바꿔야 함. int()나 float()을 이용하면 문자열 타입의 데이터를 정수나 실수 타입 으로 변환. 정수인 것을 int()를 이용해 판매량 데이터를 숫자로 변환.



커피 종류별로 생성한 빈 리스트에 항목을 추가하는 append()를 이용해 커피 종류별로 판매량 데이터를 분류.

```python
f = open(file_name)               # 파일 열기
header = f.readline()             # 데이터의 첫 번째 줄을 읽음
headerList = header.split()       # 첫 줄의 문자열을 분리한 후 리스트로 변환

espreso = []                      # 커피 종류별로 빈 리스트 생성
americano = []
cafelatte = []
cappucino = []

for line in f:                    # 두번째 줄부터 데이터를 읽어서 반복적으로 처리
    dataList = line.split()       # 문자열에서 공백을 제거해서 문자열 리스트로 변환
    
    # 커피 종류별 판매량을 정수로 변환한 후, 리스트의 항목으로 추가
    espreso.append(int(dataList[1]))
    americano.append(int(dataList[2]))
    cafelatte.append(int(dataList[3]))
    cappucino.append(int(dataList[4]))
    
f.close()                            # 파일 닫기

print('{0}: {1}'.format(headerList[1], espreso))  # 변수에 할당된 값을 출력
print('{0}: {1}'.format(headerList[2], americano))
print('{0}: {1}'.format(headerList[3], cafelatte))
print('{0}: {1}'.format(headerList[4], cappucino))
```

`Out`: 에스프레소: [10, 12, 11, 15] 

​		  아메리카노: [50, 45, 53, 49] 

​		  카페라테: [45, 41, 32, 38] 

​		  카푸치노: [20, 18, 25, 22]



리스트를 이용해 4일 메뉴별 전체 판매량과 하루 평균 판매량을 구함. 리스트, 튜플, 세트 데이터에서 항목의 합을 구하는 내장 함수 sum()과 항목의 개수(길이)를 구하는 내장 함수 len()을 이용.

```python
total_sum = [sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
total_mean = [sum(espresso)/len(espresso), sum(americano)/len(americano), sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

for k in range(len(total_sum)):
    print('[{0}] 판매량'.format(headList[k+1]))
    print('- 나흘 전체: {0}, 하루 평균: {1}'.format(total_sum[k], total_mean[k]))
    
**수정 필요**
```





## 10 모듈

> 파이썬 코드를 작성한 후 파일로 저장하면 다른 코드에서도 이 파일의 변수, 함수, 클래스를 불러와 이용할 수가 있음. 파이썬에서는 코드가 저장된 파일을 모듈(Module)이라 함. 코드를 작성할 때 이미 만들어진 모듈을 활용하면 코드를 효과적으로 작성할 수 있음.

#### 01 모듈을 사용하는 이유 

파이썬에서 모듈은 상수, 변수, 함수, 클래스를 포함하는 코드가 저장 된 파일. 모듈은 다른 모듈에서도 불러서 실행할 수도 있고 파이썬(혹은 IPython) 콘솔이나 주피터 노트북에서 불러서 실행할 수 있음.

모듈로 나누면 코드 작성과 관리가 쉬워 짐. 

• 어느 정도 규모가 큰 프로그램을 작성할 경우 파일 하나에 전체 코드를 구현하지 않고 가능별로 나눈 후에 여러 파일에서 해당 가능의 코드를 구현 

• 하나의 코드 파일에서는 해당 가능의 구현에만 신경 쓰면 되므로 코드 작성과 관리가 편해짐 

이미 작성된 코드를 재사용할 수 있음

• 특정 프로그램을 만들기 위해 작성한 모듈은 다른 코드들 만들 때도 활용할 수 있음

• 특정 가능을 구현한 모듈은 다른 프로그램을 작성할 때 재사용할 수 있음 

• 코드를 다시 만들지 않아도 되니 코드를 빨리 작성할 수 있음 

• 자신이 만든 모듈뿐 아니라 다른 사람이 만든 모듈도 사용할 수 있음

공동작업이 편리해 짐 

• 규모가 큰 프로그램을 만들 때는 일반적으로 여러 사람이 같이 작업을 진행 

• 공동으로 프로그램을 만들 때는 전체 프로그램을 모듈별로 설계하고 개인별로 나누어 코딩한 후 전체 모듈을 통합 

• 모듈별로 구분해 코드를 작성 하면 자신이 맡은 모듈만 신경 쓰면 되므로 공동 작업으 로 인한 복잡성이 줄고 효율은 높아짐



#### 02 모듈 생성 및 호출

> 모듈은 파이썬 코드가 저장된 파일. 모듈 이름은 확장자(.py)를 제외한 파일 이름. 파일로 저장된 모듈을 활용하려면 모듈이 저장된 위치(경로)에서 파이썬 (혹은 IPython) 콘솔 혹은 주피터 노트북을 실행해서 코드를 작성하거나 파이썬 코드 파일을 실행하면 됨. 모듈이 저장된 위치(경로)를 지정하는 것(모듈과 같은 위치(경로)에 있지 않더라도 모듈을 수행)

*** 모듈 만들기**

코드를 ‘모듈이름.py'로 저장. 내장 마술 명령어(magic command)인 ’%%writefile'을 이용해 코드를 파일로 저장.

 • 코드 셀의 코드를 파이썬 코드 파일로 저장하기 

```python
%%writefile [-a] file.py
<코드 블록>
```

• 저장된 파이썬 코드 파일을 불러오기 

```python
%%load file.py
```

• 파이썬 코드 파일 실행하기

```python
%%run file.py
```



```python
%%writefile C:\myPyCode\my_first_module.py
# File name: my_first_module.py

def my_function():
    print('This is my first module')
```

`Out`: Writing C:\myPyCode\my_first_module.py



```
!type C:\myPyCode\my_first_module.py
```

`Out`: # File name: my_first_module.py

​		  def my_function():
​		      print('This is my first module')



*** 모듈 불러오기**

```
import 모듈명
```

모듈을 임포트한 후에는 `모듈명.변수`, `모듈명.함수()`, `모듈명.클래스()` 와 같은 형식으로 모듈에서 정의한 내용을 사용.

```python
import my_first_module

my_first_module.my_function()
```

`Out`: This is my first module



```python
%%writefile C:\myPyCode\modules\my_area.py   # 파일명: my_area.py

PI = 3.14
def square_area(a):                           # 정사각형의 넓이 반환
    return a ** 2

def circle_area(r):                           # 원의 넓이 반환
    return PI * r ** 2
```

`Out`: Writing my_area.py

```python
import my_area                                    # 모듈 불러오기

print('pi =', my_area.PI)                         # 모듈 변수 이용
print('square_area =', my_area.square_area(5))    # 모듈 함수 이용
print('circle_area =', my_area.circle_area(2))
```

`Out`: pi = 3.14 

​		  square_area = 25 

​		  circle_area = 12.56

 불러온 모듈에서 사용할 수 있는 변수, 함수, 클래스를 알고 싶다면 `dir(모듈명)`을 이용. 

```python
dir(my_area)
```

`Out`: ['PI', 

​		  '__builtins__',       # '_'가 두개씩('__') 문자 앞뒤로 붙어 문자가 볼드체 처리됨. 

​		  '__cached__', 

​		  '__doc__', 

​		  '__file__', 

​		  '__loader__', 

​		  '__name__', 

​		  '__package__', 

​		  '__spec__', 

​		  'circle_area', 

​		  'square_area']

my_area 모듈에서 정의한 변수 PI와 함수 circle_area()와 square_area() 가 있음.



*** 모듈을 불러오는 다른 형식**

**모듈의 내용 바로 선언**

모듈 내의 변수와 함수를 호출하기 위해 `import 모듈명`으로 모듈을 불러와 `모듈명.변수`, `모듈명.함수()`와 같은 형식을 이용하였음. 이 경우 모듈 내에서 정의한 내용을 호출하기 위해 계속해서 모듈명을 써 야 하므로 코드를 작성할 때 불편함. 모듈 내에 있는 변수와 함수, 그리고 클래스를 ’모듈명.' 없이 ’변수’, '함수()', '클래스()'처럼 직접 호출해서 이용할 수 있음.

```python
from 모듈명 import 변수명
from 모듈명 import 함수명
from 모듈명 import 클래스명
```

 from 모듈명 import 변수명'형식으로 모듈에서 변수를 바로 불러와서 사용.

```python
from my_area import PI          # 모듈의 변수 바로 불러오기
print('pi =', PI)               # 모듈의 변수 이용
```

`Out`: pi = 3,14



모듈 함수를 'from 모듈명 import 함수명' 형식으로 바로 불러서 사용.

```python
from my_area import square_area          # 모듈의 변수 바로 불러오기
from my_area import circle_area

print('square_area =', my_area.square_area(5))    # 모듈 함수 이용
print('circle_area =', my_area.circle_area(2))
```

`Out`: square_area = 25 

​		  circle_area = 12.56



모듈의 변수와 함수를 이용하기 위해 `from 모듈명 import 변수명`과 `from 모듈명 import 함수명` 으로 필요한 변수와 함수 개수만큼 각각 선언해서 이용. from 모들명 import 변수명/함수명/클래스명'은 하나만 선언할 수 있 는 것이 아니라 콤마(,)로 구분해서 여러 개를 선언할 수 있음.

```python
from my_area import PI, square_area, circle_area

print('pi =', PI)  
print('square_area =', my_area.square_area(5))    # 모듈 함수 이용
print('circle_area =', my_area.circle_area(2))
```

`Out`: pi = 3.14 

​		  square_area = 25 

​		  circle_area = 12.56



모듈의 모든 변수, 함수, 클래스를 바로 모듈명 없이 바로 이용.

```python
from 모듈명 import *
```

```python
from my_area import *

print('pi =', PI)  
print('square_area =', my_area.square_area(5))    # 모듈 함수 이용
print('circle_area =', my_area.circle_area(2))
```

`Out`: pi = 3.14 

​		  square_area = 25 

​		  circle_area = 12.56



※ from 모듈명 import *' 형식으로 선언하는 방법은 '모듈명.'을 쓰지 않고 모듈 내의 변수, 함수, 클래스를 사용할 수 있어서 편리하기는 하 지만 **모듈을 두 개 이상 이용할 때는 주의가 필요.**

```python
%%writefile C:\myPyCode\modules\my_module1.py 
# File name: my_module1.py 

def func1():
    print('func1 in my_module1 ')
    
def func2():
    print('func2 in my_module1 ')
```

`Out`: Writing C:\myPyCode\modules\my_module1.py 

```python
%%writefile C:\myPyCode\modules\my_module2.py 
# File name: my_module2.py 

def func2():
    print('func2 in my_module2 ')
    
def func3():
    print('func3 in my_module2 ')
```

`Out`: Writing C:\myPyCode\modules\my_module2.py 



```python
from my_module1 import*
from my_module2 import*

func1()
func2()
func3()
```

`Out`: func1 in mu_module1  

​		  func2 in mu_module2  

​		  func3 in mu_module2 

코드는 오류 없이 잘 수행. 모듈 my_module1과 모듈 my_module2에만 각각 존재하는 func1과 func3은 불러오는데 문제가 없음. **모듈 my_module1 과 모듈 my_module2에 모두 있는 func2 함수를 호출하면 나중에 선언해서 불러온 모듈의 함수가 호출됨.**



```python
from my_module2 import*
from my_module1 import*

func1()
func2()
func3()
```

`Out`: func1 in mu_module1  

​		  func2 in mu_module1  

​		  func3 in mu_module2 

 func2()를 호출했을 때 이번에는 my_module1 모듈에서 함수를 불러 온 것을 알 수 있음.



*** 모듈 명을 별명으로 선언**

`import 모듈명` 형식으로 모듈을 선언해서 이용할 경우 '모듈명.변수', '모듈명.함수()'，'모듈명.클래스()'와 같은 형식으로 모 듈에서 정의한 내용을 불러오는데 코드에서 매번 모듈명을 입력하기 가 번거로움. 특히 모듈명이 길다면 입력이 더욱 번거로울 것. `from 모듈명 import *` 방법으로 선언해서 `모듈명.`을 생략할 수도 있지만 여러 모듈을 임포트할 경우에는 주의가 필요.

 모듈명에 새로운 이름{별명)을 붙이면 해결 

```python
import 모듈명 as 별명
```

코드를 작성할 때 `모듈명.변수`, `모듈명.함수()`, `모듈명.클래스()`  대신 `별명.변수`,`별명.함수()`, `별명.클래스()`처럼 지정 할 수 있음.

 모듈뿐 아니라 변수명, 함수명, 클래스명도 별명을 붙일 수 있음.

```python
from 모듈명 import 변수명 as 별명 
from 모듈명 import 함수명 as 별명 
from 모듈명 import 클래스명 as 별명
```

 변수명, 함수명, 클래스명 대신 별명으로 이용할 수 있음.

```python
import my_area as area             # 모듈명(my_area)에 별명(area)을 붙임.

print('pi =', PI)                  # 모듈명 대신 별명 이용
print('square_area =', area.square_area(5))   
print('circle_area =', area.circle_area(2))
```

`Out`: pi = 3.14 

​		  square_area = 25 

​		  circle_area = 12.56

```python
from my_area import PI as pi
from my_area import square_area as square
from my_area import circle_area as circle

print('pi =', PI)                  # 모듈 변수의 별명 이용
print('square_area =', square(5))  # 모듈 함수의 별명 이용 
print('circle_area =', circle(2))
```

`Out`: pi = 3.14 

​		  square_area = 25 

​		  circle_area = 12.56



#### 03 모듈을 직접 실행하는 경우와 임포트한 후 실행하는 경우 구분하기

`import 모듈명`로 불러온 후에 모듈과 관련된 코드를 실행해야 결과를 확인할수 있었음. 모듈을 만들 때는 함수나 클래스가 잘 작성됐는지 확인하기 위해 모듈 내에서 함수나 클래스를 직접 호출.

```python
%%writefile C:\myPyCode\modules\my_module_test1.py 
# File name: my_module_test1.py

def func(a):
    print("입력숫자: ", a)
    
func(3)
```

`Out`: Writing c:\myPyCode\modules\my_module_test1.py

```python
%run C:\myPyCode\modules\my_module_test1.py
```

`Out`: 입력숫자: 3

```python
import my_module_test1
```

`Out`: 입력숫자: 3

`import 모듈명`을 통해 모듈을 불러오면 모듈 내의 코드를 실행됨. `import my_module_test1`를 수행하면 my_module_test1 모듈의 코 드가 수행. my_module_test1 모듈 내 코드에서 func(3)는 작성한 함수가 잘 실행되는지를 확인하기 위해 작성해 놓은 것이지 모듈을 임포트할 때 실 행하기 위해 작성한 코드가 아님.  모듈을 마지막으로 저장 할 때는 테스트를 위해 작성한 코드는 삭제. 테스트를 위해 작성한 코드를 일일이 삭제하는 것은 번거로움. 모듈을 테스트하기 위해 직접 수행하는 경우와 임포트해서 사용하는 경우를 구분.



 모듈을 마지막으로 저장 할 때는 테스트를 위해 작성한 코드는 삭제. 테스트를 위해 작성한 코드를 일일이 삭제하는 것은 번거로움. 모듈을 테스트하기 위해 직접 수행하는 경우와 임포트해서 사용하는 경우를 구분 모듈을 마지막으로 저장 할 때는 테스트를 위해 작성한 코드는 삭제. 테스트를 위해 작성한 코드를 일일이 삭제하는 것은 번거로움. 모듈을 테스트하기 위해 직접 수행하는 경우와 임포트해서 사용하는 경우를 구분.



 모듈을 직접 수행하는 경우와 임포트해서 이용하는 경우를 구분해 사용.

```python
if __name__ == "__main__": 
    〈직접 수행할 때만 실행되는 코드〉
```

코드를 모듈 파일에서 직접 수행하느냐 아니면 임포트해서 사용하느냐 에 따라 코드를 다르게 수행. 같은 모듈에서 코드를 직접 수행할 때만 `if __name__ == "__main__"： ` 안의 코드가 실행되고 임포트해서 사용하면 수행되지 않음.

```python
%%writefile C:\myPyCode\modules\my_module_test2.py
# File name: my_module_test2.py

def func(a):
    print('입력 숫자:', a)
    
if __name__=="__main__":
    print('모듈을 직접 실행')
    func(3)
    func(4)
```

`Out`: Writing c:\myPyCode\modules\my_module_test2.py

```python
%run c:\myPyCode\modules\my_module_test2.py
```

`Out`: 모듈을 직접 실행

​		  입력 숫자: 3

​		  입력 숫자: 4



```python
import my_module_test2
```

실행 결과를 보면 아무것도 출력되지 않음. `if __name__ == "__main__"：` 내에 작성한 코드는 임포트한 경우에는 실행되지 않기 때문.

모듈에서 코드를 직접 수행하는 경우와 임포트해서 사용하는 경우를 구분해서 코드를 실행하기 위한 구조.

```python
if __name__ == "__main__"：
	< 직접 수행할 때만 실행되는 코드> 
else: 
    < 임포트됐을 때만 실행되는 코드>
```



```python
%%writefile C:\myPyCode\modules\my_module_test3.py
# File name: my_module_test3.py

def func(a):
    print('입력 숫자:', a)
    
if __name__=="__main__":
    print('모듈을 직접 실행')
    func(3)
    func(4)
else:
    print('모듈을 임포트해서 실행')
```

`Out`: Writing c:\myPyCode\modules\my_module_test3.py

```python
%run c:\myPyCode\modules\my_module_test3.py
```

`Out`: 모듈을 직접 실행

​		  입력 숫자: 3

​		  입력 숫자: 4

```python
import my_module_test3
```

`Out`: 모듈을 임포트해서 실행



#### 04 내장 모듈

> 임의로 숫자(난수)를 발생시키는 random 모듈, 날짜 및 시간 관련 처리할 수 있는 datetime 모듈，연도/월/주 등 달력과 관련된 처리를 할 수 있는 calendar 모듈을 이 용하는 방법. 파이썬 표준 라이브러리에 관해 설명 한 사이트 https://docs.python.org/3.9/library

***난수 발생 모듈**

코드에서는 정해진 숫자가 아닌 실행할 때마다 임의의 숫자를 사용해 야 할 때가 있음. 임의의 숫자를 난수(random number) 라고함. 파이썬에서는 random 모듈을 이용해 난수를 만들 수 있음. random 모듈을 이용하려면 `import random`으로 random 모듈을 먼저 불러온 후에 random 모듈의 함수를 이용.

```python
import random 
random.random모듈함수()
```



```python
import random 

random.random()
```

`import random`으로 random 모듈을 불러왔고 `random.random()`으로 0~1 사이의 실수중에서 임의의 숫자를 생성. random은 모듈명이고 random()은 random 모듈의 함수. random.random()를 실행할 때마다 다른 값이 출력. random.random() 코드를 실행하면 결과가 다를 것(난수를 발생시키 는 함수의 특징).

randon 모듈의 함수와 사용 예

| random 모듈의 함수          | 설명                                                         | 사용 예                           |
| --------------------------- | ------------------------------------------------------------ | --------------------------------- |
| random()                    | 0.0 <= 실수 < 1.0 범위의 임의의 실수를 반환                  | random.random()                   |
| randint(a, b)               | a <= 정수 <= b의 범위의 임의의 정수 반환                     | random.randint(1, 6)              |
| radrange(start, stop, step) | range(start, stop, step)에서 임의의 정수를 반환              | random.radrange(0, 10, 2)         |
| choice(seq)                 | 공백이 아닌 시퀸스(seq)에서 임의의 항목을 반환               | random.choice([1, 2, 3])          |
| sample(population, k)       | 시퀸스로 이뤄진 모집단(population)에서 중복되지 않는 k개의 인자를 반환 | random.sample([1, 2, 3, 4, 5], 2) |

특정 범위의 정수 안에서 임의의 정수를 발생시키려면 randint() 함수를 이용. 

숫자가 1에서 6까지 있는 주사위 두 개를 던져서 두 개의 숫자가 임의로 나오게 하는 코드.

```python
import random

dice1 = random.randint(1, 6)   # 임의의 정수가 생성됨.
dice2 = random.randint(1, 6)   # 임의의 정수가 생성됨.
print('주사위 두개의 숫자: {0}, {1}'.format(dice1, dice2))
```

`Out`: 주사위 두개의 숫자: 4, 2

```python
import random

random.randrange(0, 11, 2)
```

`Out`: 6

```python
import random

num1 = random.randrange(1, 10, 2)   # 1 ~ 9 중 임의의 홀수 선택
num2 = random.randrange(1, 100, 10) # 1 ~ 99 중 임의의 10 단위 숫자 선택
print('num1: {0}, num2: {1}'.format(num1, num2))
```

`Out`: num1: 3, num2: 61

```python
import random

menu = ['비빔밥', '된장찌개', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
random.choice(menu)
```

`Out`: '불고기' 

````python
import random

random.sample([1, 2, 3, 4, 5, 6], 2)  # 모집단에서 두개의 인자 선택
````

`Out`: 4, 6



*** 날짜 및 시간 관련 처리 모듈**

날짜와 시간을 다룰 수 있는 파이썬 내장 모듈인 datetime 모듈. datetime 모듈에는 날짜를 표현하는 date 클래스, 시간을 표현하는 time 클래스, 날짜와 시간을 표현하는 datetime 클래스 등이 있음. datetime 모듈을 이용하려면 먼저 `import datetime`으로 datetime  모둘을 불러와야 함. datetime 모듈을 불러온 후에는 클래스에서 객체를 생성해 이용하는 방법이 있고 각 클래스의 클래스 메서드를 이용하는 방법.

datetime 모듈의 각 클래스에서 객체를 생성해 이용하는 방법 

```python
import datetime 

date_obj = datetime.date(year, month, day) 
time_obj = datetime.time(hour, minute, second) 
datetime_obj = datetime.datetime(year, month, day, hour,  minute, second)
```

 생성한 객체를 이용해 각 클래스의 속성을 이용. date 클래스에는 year, month, day의 속성이 있으며 time 클래스에 는 hour, minute, second의 속성이 있음. datetime 클래스는 date 클래스라 time 클래스의 모든 속성이 있음.

내장 모듈 datetime을 이용하는 다른 방법은 객체를 생성하지 않고 각 클래스의 클래스 메서드를 이용 하는 것.

```python
import datetime 

date_var = datetime.date.date_classmethod() 
time_var = datetime.time.time.classmethod() 
datetime_var = datetime .datetime .datetime_classmethod()
```

클래스 메서드를 이용하는 경우에도 각 클래스의 속성은 그대로 이용.

날짜를 표현하는 date 클래스.

```python
import datetime

set_day = datetime.date(2021, 8, 4)
print(set_day)
```

`Out`: 2021-08-04

 date 객체를 생성할 때 인자로 연도, 월, 일을 입력할 수 있음. 생성된 date 객체는 print()로 입력한 날짜를 출력. 연도, 월, 일을 각각 구하려면 date 클래스의 속성(year, month, day) 을 이용.

```python
print('{0}/{1}/{2}'.format(set_day.year, set_day.month, set_day.day))
```

`Out`: 2021/8/4

datetime 모듈의 date 객체는 타입이 date로 그 객체끼리 빼기 연산 을 할 수 있음. 빼기 연산에서 앞의 객체의 날짜가 뒤의 객체의 날짜보다 더 나중이면 결과 날짜가 양수로 나오고 더 먼저이면 결과 날짜가 음수로 나옴. 빼기 연산을 수행한 후에 결과의 데이터 타입은 timedelta로 바뀜.

```python
import datetime

day1 = datetime.date(2021, 4, 1)
day2 = datetime.date(2021, 8, 4)
diff_day = day2 - day1
print(diff_day)
```

`Out`: 125 days, 0:00:00

데이터 타입 확인

```python
type(day1)
```

`Out`: datetime.date

```python
type(diff_day)
```

`Out`: datetime.timedelta

앞의 두 날짜차이 계산에서 날짜만 출력하려면 timedelta 클래스 속성 인 days를 이용.

```python
print('**지정된 두 날짜의 차이는 {}일 입니다 **'.format(diff_day.days))
```

`Out`: **지정된 두 날짜의 차이는 125일 입니다 **  # 마크다운 문법 때문에 강조로 보임.

datetime 모듈의 date 클래스에는 오늘 날짜를 반환하는 클래스 메서 드인 today()를 제공. 오늘 날짜를 확인(클래스 메서드 today()는 인자 없이 호출).

```python
import datetime

print(datetime.date.today())
```

`Out`: 2021-08-04

오늘과 특정 날짜의 차이를 알려면 빼기 연산을 수행

```python
import datetime

today = datetime.date.today()
special_day = datetime.date(2018, 12, 31)
print(special_day - today)
```

`Out`: -947 days, 0:00:00

시간(시각)과 관련된 처리할 수 있는 time 클래스. tine 클래스에서 객체를 생성할 때 시, 분, 초를 인자로 입력.

```python
import datetime

set_time = datetime.time(15, 30, 45)
print(set_time)
```

`Out`: 15:30:45

 time 클래스의 속성(hour, minute, second)을 이용해 시, 분, 초를 각 각 출력.

```python
print('{0}:{1}:{2}'.format(set_time.hour, set_time.minute, set_time.second))
```

`Out`: 15:30:45

날짜와 시간을 모두 다룰 수 있는 datetime 클래스.

```python
import datetime

set_dt = datetime.datetime(2018, 10, 9, 10, 20, 0)
print(set_dt)
```

`Out`: 2018-10-09 10:20:00

`import datetime`의 datetime은 모듈 이름이고 datetime()은 datetime 모듈 안에 있는 클래스 이름. **모듈 이름과 클래스 이름이 같아서 혼동될 수 있는데 다른 것이니 사용 할 때 주의.**

 datetime 클래스의 경우에도 속성을 이용해 연, 월，일，시, 분, 초를 각각 수행.

```python
print('날짜 {0}/{1}/{2}'.format(set_dt.year, set_dt.month, set_dt.day))
print('시각 {0}:{1}:{2}'.format(set_dt.hour, set_dt.minute, set_dt.second))
```

`Out`: 날짜 2018/10/9 

​		  시각 10:20:0

현재 시각을 구하려면 datetime 클래스의 클래스 메서드인 now()를 이용.

```python
import datetime

now = datetime.datetime.now()
print(now)
```

`Out`: 2021-08-04 02:47:12.205788

now()로 얻은 결과는 오늘 날짜(연, 월, 일)와 현재 시각(시, 분, 초). 초는 소수점 이하의 초까지 반환.

 각 클래스의 속성을 이용해 날짜와 시간을 출력했지만 날짜 및 시간 출력 양식을 지정해 출력.

```python
print('Date & Time: {:%Y-%h-%d, %H:%M:%S}'.format(now))
```

`Out`: Date & Time: 2021-Aug-04, 02:47:12

%Y, %m, %d는 각각 연도, 월, 일을 나타내고 %H, %M, %S는 각각 시, 분, 초를 나타냄. 이 값들은 `{: }` 안에 있어야 하며 일부만 사용할 수도 있음.

날짜와 시각을 각각 출력.

```python
print('Date: {:%Y, %m, %d}'.format(now))
print('Time: {:%H/%M/%S}'.format(now))
```

`Out`: Date: 2021, 08, 04 

​		  Time: 02/47/12

date 클래스의 객체와 마찬가지로 datetime 클래스의 객체도 빼기 연산을 할 수 있음.  현재 날짜 및 시각과 특정일의 날짜 및 시각의 차이를 구하기.

```python
now = datetime.datetime.now()
set_dt = datetime.datetime(2017, 12, 1, 12, 30, 45)

print('현재 날짜 및 시각: ', now)
print('차이: ', set_dt - now)
```

`Out`:  현재 날짜 및 시각:  2021-08-04 04:43:45.691644 

​		  차이:  -1342 days, 7:46:59.308356

datetime 모듈의 객체를 `import 모듈명`을 수행한 후에 사용했지만 `from 모듈명 import 클래스명` 방법을 이용하면 모듈명 없이 바로 클래스 이름이나 클래스 메서드 이름으로 이용할 수 있음.

```python
from datetime import date, time, datetime

print(date(2019, 7, 1))
```

`Out`: 2019-07-01

```python
print(date.today())
```

`Out`: 2021-08-04

```python
print(time(15, 30, 45))
```

`Out`: 15:30:45

```python
print(datetime(2020, 2, 14, 18, 10, 50))
```

`Out`: 2020-02-14 18:10:50

```python
print(datetime.now())
```

`Out`: 2021-08-04 04:50:41.078634



*** 달력 생성 및 처리 모듈**

파이썬 내장 모듈인 calendar 모듈을 이용해 다양한 형태로 달력을 생 성해 출력하고 날짜와 관련된 정보(연도, 월, 주)를 구하는 방법. calendar 모듈은 달력과 관련된 클래스와 함수를 제공.

● calendar 모듈의 주요 함수 및 사용 예

| calendar 모듈의 함수      | 설명                                                         | 사용 예                            |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------- |
| calendar(year)            | 지정된 연도(year)의 전체 달력을 문자열로 반환(기본 형식은 3개의 열) | calendar.calendar(2017)            |
| month(year, month)        | 지정된 연도(year)와 월(month)의 달력을 문자열로 변환         | calendar.month(2019, 1)            |
| monthrange(year, month)   | 지정된 연도(year)와 월(month)의 시작 요일과 일수 반환. 요일의 경우 0(월요일) ~ 6(일요일) 사이의 숫자로 반환 | calendar.monthrange(2020, 1)       |
| firstweekday()            | 달력에 표시되는 주의 첫 번째 요일값을 반환. 기본값으로는 월요일(0)으로 지정 | calendar.firstweekday()            |
| setfirstweekday(weekday)  | 달력에 표시되는 주의 첫번째 요일을 지정                      | calendar.setfirstweekday(6)        |
| weekday(year, month, day) | 지정된 날짜[연도(year), 월(month), 일(day)]의 요일을 반환    | calendar.weekday(year, month, day) |
| isleap(year)              | 지정된 연도(year)가 윤년인지를 판단하 윤년이면 True, 아니면 False를 반환 | calendar.isleap(2020)              |

● calendar 모듈에서 요일 지정 상수

| 요일 | 요일 지정 상수     | 숫자로 표시 |
| ---- | ------------------ | ----------- |
| 월   | calendar.MONDAY    | 0           |
| 화   | calendar.TUESDAY   | 1           |
| 수   | calendar.WEDNESDAY | 2           |
| 목   | calendar.THURSDAY  | 3           |
| 금   | calendar.FRIDAY    | 4           |
| 토   | calendar.SATURDAY  | 5           |
| 일   | calendar.SUNDAY    | 6           |

 calendar 모듈을 이용하려면 먼저 `import calendar`로 모듈을 불러 와야 함.

calendar() 함수를 이용해 지정한 연도의 전체 달력을 출력하는 방법.

```python
import calendar

print(calendar.calendar(2018))
```

`Out`: ![달력 출력 내용 캡쳐]()



calendar() 함수의 기본적인 달력 출력 양식은 달을 3열로 출력.





```
print(calendar.calendar(2019, m=4))
```

`Out`: <img src="c:\myPyCode\Png file\10-04-01.png" alt="달력 출력 내용 캡쳐" style="zoom:33%;" />

```python
print(calendar.month(2020, 9))
```

`Out`: <img src="C:\myPyCode\Png file\10-04-02.png" style="zoom:33%;" />  

연도와 월을 지정해 그달 1일이 시작하는 요일과 그달의 날짜 수를 알 고 싶다면 monthrange()함수를 이용

```python
print(calendar.monthrange(2020, 2))
```

`Out`: (5, 29)

결과로 두 개의 숫자가 반환. 첫 번째 숫자는 해당 월의 1일의 요일에 해당하는 숫자{월요일 ~ 일요 일을 의미하는 0〜 6 중 하나가 반환됨). 두 번째 숫자는 해당 월의 날짜 수. 출력된 달력을 보면 일주일의 시작 요일이 월요일인 것을 알 수 있음.

달력에서 일주일의 시작 요일을 구하려면 firstweekday() 함수를 실행.

```python
calendar.firstweekday()
```

`Out`: 0

결과로 0이 출력돼 달력에서 일주일의 시작 요일이 월요일로 지정됨.

시작 요일을 지정하려면 setfirstweekday(weekday) 함수를 이용. 시작 요일을 일요일로 지정하려면 weekday 에는 6(혹은 calendar.SUNDAY)을 입력. 

setfirstweekday (calendar.SUNDAY) 로 달력에서 일주일의 시작 요 일을 일요일로 바꾸고 달력을 출력.

```python
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2020, 9))
```

`Out`: <img src="C:\myPyCode\Png file\10-04-03.png" style="zoom: 33%;" />

```python
print(calendar.weekday(2018, 10, 14))
```

`Out`: 6

```python
print(calendar.isleap(2018))
print(calendar.isleap(2020))
```

`Out`: False

​		  True



#### 05 패키지

> 파이썬에서 모듈은 코드가 저장된 파일. 어떤 기능을 구현할 때 하나의 모듈로 구성하 기보다는 여러 개의 모듈 로 구현하는 경우가 많음. **여러 모듈을 체계적으로 모아서 꾸러미로 관리하면 편리. 파이썬에서는 이런 꾸러미를 패키지(Package)라고 함.** 파이썬 패키지는 여러 모듈을 폴더로 묶어서 계충적으로 관리. 복잡하고 규모가 큰 프로그램을 작성할 때는 각 모듈을 묶어서 패키지 로 만들면 좀 더 효율적으로 코드를 관리할 수 있음.

*** 패키지의 구조**

파이썬 패키지는 폴더 구조로 돼 있으며 각 폴더에는 `__init__.py`라는 특별한 파일이 있음. `__init__.py` 파일은 해당 폴더가 패키지의 일부인 것을 알려주는 역할을 함. `__init__.py` 파일은 패키지를 초기화하는 코드를 넣을 수도 있고 아무 코드도 없는 빈 파일일 수도 있음. 패키지를 만들 때 `__init__.py` 파일이 없어도 되지만 하위 호환성을 고 려하면 `__init__.py`파일을 포함하는 것이 좋음.

● image 패키지의 폴더 구조 예시

```
\---image
	|	__init__.py
	|
	+---efect
	|	  rotate.py
	|	  zoomInOut.py
	|	  __init__.py
	|
	+---filter
	|	  blur.py
	|	  sharpen.py
	|	  __init__.py
	|
	\---io_file
			imgread.py
			imgwrite.py
			__init__.py
```



*** 패키지 만들기**

imgread 모듈에는 pngread() 함수와 jpgread() 함수를 만듬.

```python
%%writefile c:\myPyCode\packages\image\io_file\amgread.py
# File name: imgread.py

def pngread():
    print('pngread in imgread module')
    
def jpgread():
    print('jpgread in imgread module')
```





*** 패키지 사용하기**

패키지 모듈을 이용하려면 `import 패키지 내 모듈명`으로 선언. 패키지명에서 시작해 모듈명까지 구분하기 위해 패키지명, 폴더명, 모 듈명 사이에 온점(.)을 입력. 패키지 폴더 안에 바로 모듈이 있다면 `import 패키지명.모들명`으로 모듈을 호출. 패키지와 모듈 사이에 폴더가 있다면 `import 패키지명.폴더명.모둘명` 으로 모듈을 호출.

패키지에서 모듈 내의 함수를 호출하는 방법.

```python
import image.io_file.imgread  # image 패키지 io_file 폴더의 imgread 모듈 임포트

import image.io_file.pngread  # imgread 모듈 내의 pngread() 함수 호출
import image.io_file.jpgread  # imgread 모듈 내의 jpgread() 함수 호출
```

`Out`



`from A import B` 형식을 이용하면 패키지 안에 있는 모듈 내 함수를 더 간단하게 호출. 첫 번째 방법은 `from A import B`에서 A에는 `패키지명[.폴더명]`을 입력하고 B에는 사용할 모듈명을 입력.

```python
from image.io_file import imgread  

imageread.pngread()
imageread.jpgread()
```

`Out`





```
```


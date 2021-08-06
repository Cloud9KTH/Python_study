# NumPy

*** 배열 생성하기**

NumPy는 파이썬 모듈이 아님. 사용하려면 따로 설치가 필요함. 아나콘다 배포판에는 포함되어 있음. 설치된 NumPy를 사용하려면 NumPy 패키지를 불러와야됨.

```python
import numpy as np
```

※ 위와 같이 불러오면 별명 형식으로 불러와서 `np`로 호출 가능.



**시퀸스 데이터로부터 배열 생성**

```python
arr_obj = np.array(seq_data)
```

시퀸스 데이터(seq_data)를 인자로 받아 NumPy의 배열 객체(array object)를 생성함. 시퀸스 데이터(seq_data)로 리스트와 튜플 타입의 데이터 모두 사용 가능하나, 주로 리스트 데이터 사용.

```python
import numpy as np
data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
a1
```

```
Out:
array([0, 1, 2, 3, 4, 5])
```


# 1. 파일을 생성하여 여는 `open` 명령어 처음 배워 사용
# 2. 파일 생성후 쓰기 및 닫기 하는 메써드 `.write() ; .close()` 사용
# --> `.write()` 메써드는 한 명령어에 딱 하나의 개체만 입력을 하기에 
# 처음에는 잘 몰라서 오류 많이 발생하고 디버깅하며 제대로 코드를 만듦.
# 그리하여 `.write()` 함수를 많이 씀.
# 3. 파일에 쓰기 메써드의 경우, 입력을 여러번 해도 줄 바꿈이 안되어 
# 줄바꿈을 위해 `\n` 사용. 그리고 `\n`을 적절하게 넣는것을 고민 했음.

# ▶ 간단한 코드지만, `range()`의 숫자 범위를 조정하여 단수 변경이 
# 용이하고(15단, 20단 까지 가능) 곱셈할때 ? X 9 이후의 숫자도 가능
# (? X 12)

f = open('multiplication.txt', 'w')
f.write('곱셈표 생성\n')
for a in range(2, 10) :
    f.write('\n<')
    f.write(str(a))
    f.write('단 >\n')
    for b in range(1, 10):
        f.write( str(a) )
        f.write('X' )
        f.write(str(b) )
        f.write('=' )
        f.write(str(a*b))
        f.write('\n')
f.close()
# 버스 요금 출력하는 프로그램을 만드는 과제가 있어 `if`, `elif`, `else`
# 제어문을 활용하여 아래와 같은 함수 형태로 프로그램을 만들고 실행 시킴.

def bus_fare_cal(age, pay):
    print('나이:', age)
    if pay == '현금' :
        print('지불방식:', pay)       
        if 0< age < 8:
            fare = '무료'
        elif age <= 13 :
            fare = 450
        elif age <= 19 :
            fare = 1000
        elif 20 <= age <75:
            fare = 1300        
        else :
            fare = '무료'
        print('버스 요금은', fare,'원 입니다.')
    elif pay == '카드' :
        print('지불방식:', pay)       
        if 0< age < 8:
            fare = '무료'
        elif age <= 13 :
            fare = 450
        elif age <= 19 :
            fare = 720
        elif 20 <= age <75:
            fare = 1200        
        else :
            fare = '무료'
        print('버스 요금은', fare,'원 입니다.')
  

bus_fare_cal(75, '카드')

# 아래도 함수 형태로 만들었으나, 실행 시키면 문자열 입력 받아 실행되는
# 프로그램을 함수형태로 구현 연습 해봄.
# 프로그램 코딩을 할때, "Jupyter notebook"을 활용하면, 셀 단위로
# 바로바로 실행시켜보고 오류(traceback)을 자세하게 확인이 가능하여
# "Jupyter notebook"도 같이 활요하고 있음.

def bus_fare_cal() :
    age = float(input('몇살인가요?'))    
    if age <= 13 :
        fare = 800    
    elif age <= 19 :
        fare = 1300
    else :
        fare = 1600
    pay = input('현금 or 카드?')
    if pay == '현금' :
        print('버스 요금은', fare,'원 입니다.')
    elif pay == '카드' :
        print('버스 요금은', fare - 50,'원 입니다.')

bus_fare_cal()
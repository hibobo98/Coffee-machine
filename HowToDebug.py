'''디버깅 Debugging
버그를 하나씩 잡아가는 과정 
- break point(중단점) 찍고, F5
- Variables에서 각 변수에 담긴 정보 알 수 있음
- Watch에서 변수, 함수를 검색해서 정보를 얻을 수도 있음 
- Call Stack : 어디로부터 호출되는 건지 추적 가능 

'''


def say_hi(num):
    num += 1
    return num


say_hi(1)

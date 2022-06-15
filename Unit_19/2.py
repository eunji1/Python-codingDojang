#별 출력 다르게 해보기
num = int(input())
def StarMake(num):
    string = ''
    for i in range(num):
        print(string.ljust(num-i)+'*'+'*'*i*2)
#ljust는 왼쪽부터 반복할 횟수 만큼 문자열 출력
StarMake(num)
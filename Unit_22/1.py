'''
표준 입력으로 정수 두 개가 입력됩니다
(첫 번째 입력 값의 범위는 1~20, 
두 번째 입력 값의 범위는 10~30이며 
첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요
(input에서 안내 문자열은 출력하지 않아야 합니다). 
단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 
출력 결과는 리스트 형태라야 합니다.
'''
start, stop = map(int, input().split())
def PowerN(start, stop):
    listN = [2 ** i for i in range(start, stop+1)]
    del listN[1], listN[-2]
    return listN

listN = PowerN(start, stop)
print(listN)
# start, stop =map(int,input().split())
# list_a=[2 ** i for i in range(start, stop + 1)]
# del list_a[1], list_a[-2]
# print(list_a)
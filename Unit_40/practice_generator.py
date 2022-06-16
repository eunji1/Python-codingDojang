def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')

for i in file_read():
    print(i)

'''
용량이 매우 큰 파일은 메모리에 한꺼번에 읽어서 처리하기가 힘듦 
따라서 대용량 데이터를 부분부분 처리해야 할 때 이렇게 제너레이터를 활용
'''
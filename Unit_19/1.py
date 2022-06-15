star_num = int(input())

for i in range(star_num):
    for j in reversed(range(star_num)):
        if j > i:
            print(" ", end = "")
        else:
            print("*", end = "")
    for j in range(star_num):
        if j < i:
            print('*', end='')
    print()
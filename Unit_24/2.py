#'{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'
price = list(map(int,input().split(';')))
high_price = sorted(price, reverse=True)
for i in high_price:
    print('{0: >9,}'.format(i))
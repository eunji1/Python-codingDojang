# -*- coding: utf-8 -*-
age = int(input())
balance = 9000    # 교통카드 잔액

if age >= 19:
    balance -= 1250
elif age >= 13:
    balance -= 1050
elif age >= 7:
    balance -= 650

print(balance)

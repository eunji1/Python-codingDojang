'''
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
'''
key = input().split()
value = map(float, input().split())
#status = list(zip(key,value))
#[('health', 575.6), ('health_regen', 1.7), ('mana', 338.8), ('mana_regen', 1.63)]
status = dict(zip(key,value))
print(status)
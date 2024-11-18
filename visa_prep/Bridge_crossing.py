X, Y, Z = map(int, input().split())
available_capacity = Z - Y
if available_capacity >= 0:
    max_mangoes = available_capacity // X
else:
    max_mangoes = 0
print(max_mangoes)

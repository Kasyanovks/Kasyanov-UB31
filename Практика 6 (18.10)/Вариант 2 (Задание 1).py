n=int(input()) #количество элементов в массиве
n=[int(input()) for i in range(n)] #создаем массив
print(min(n)) #находим минимальное значение
print(n.index(min(n))) #находим индекс минимального
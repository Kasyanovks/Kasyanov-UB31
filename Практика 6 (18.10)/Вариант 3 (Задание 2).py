n=[int(input()) for i in range(8)] #создаем массив с клавиатуры длинной 8
for j in range(len(n)): #перебираем все элементы массива
    if n[j]<15:
        n[j]=n[j]*2 #если элемент меньше 15, заменяем его удвоенным произведением самого себя
print(n)
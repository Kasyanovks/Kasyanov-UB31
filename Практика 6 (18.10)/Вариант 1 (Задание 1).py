n=int(input()) #колличество элементов массива
n=[int(input()) for i in range(n)] #создаем массив
print(max(n)) #ищем максимальный элемент
print(n[::-1]) #разворачиваем массив
# объявление функции
def is_pangram(text):
    s=text.lower()
    for i in 'qwertyuiopasdfghjklzxcvbnm':
        if i in s:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        return True
    else:
        return False


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))



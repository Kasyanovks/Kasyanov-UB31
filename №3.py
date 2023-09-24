#Проверка цифр в числе на четность и не четность
a=input()
chetny=[]
nechetny=[]
for b in a:
    if int(b)%2==0 and int(b)!=0:
        chetny.append(b)
    elif int(b)%2==1 and int(b)!=0:
        nechetny.append(b)
print(chetny, ' Четные')
print(nechetny, ' Не четные')
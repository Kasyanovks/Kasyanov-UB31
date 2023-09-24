#Пробное задание из лекции
d=int(input())
e=int(input())
a=int(input())
b=int(input())
c=int(input())
n=[]
if d<=a<=e or e<=a<=d:
    n.append(a)
if d<=b<=e or e<=b<=d:
    n.append(b)
if d<=c<=e or e<=c<=d:
    n.append(c)
print(n)
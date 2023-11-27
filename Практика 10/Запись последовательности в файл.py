from random import randint
n = int(input())
m = int(input())
a = []
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
f = open(r'C:\Users\konst\OneDrive\Документы\Языки програмирования\Програмирование', 'w')
for i in a:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write("\n")
f.close()

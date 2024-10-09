x = int(input("Введи целое положительное число: "))
if x<0:
    print("Факториал не найден")
i=0
factorial = 1
while i<x:
    i+=1
    factorial *= i

print("Факториал числа",x,"равен: ",factorial)
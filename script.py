import math

print("=== Твой помощник по алгебре ===")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

# Считаем дискриминант
D = b**2 - 4*a*c
print(f"Дискриминант (D) = {D}")

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Уравнение имеет один корень: x = {x}")
else:
    print("Дискриминант меньше нуля, корней нет!")

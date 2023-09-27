import math
print("Choose an option: ")
print("1. a+b")
print("2. a-b")
print("3. a*b")
print("4. a/b")
print("5. a^b")
print("6. sqrt(a)")
print("7. a!")
print("8. sin(a)")
print("9. cos(a)")
print("10. tg(a)")
s = 0
while s < 11:
    s = int(input())
    if s == 1:
        print("Type in first and second number")
        a = int(input())
        b = int(input())
        print(a, "+", b, "=", (a+b))
        s = 0
    if s == 2:
        print("Type in first and second number")
        a = int(input())
        b = int(input())
        print(a, "-", b, "=", (a-b))
        s = 0
    if s == 3:
        print("Type in first and second number")
        a = int(input())
        b = int(input())
        print(a, "*", b, "=", (a*b))
        s = 0
    if s == 4:
        print("Type in first and second number")
        a = int(input())
        b = int(input())
        print(a, "/", b, "=", (a/b))
        s = 0
    if s == 5:
        print("Type in first and second number")
        a = int(input())
        b = int(input())
        print(a, "^", b, "=", (a**b))
        s = 0
    if s == 6:
        print("Type in first number")
        a = int(input())
        c = math.sqrt(a)
        print("sqrt(", a, ")", "=", c)
        s = 0
    if s == 7:
        print("Type in first number")
        a = int(input())
        c = math.factorial(a)
        print(a,"!", "=", c)
        s = 0
    if s == 8:
        print("Type in first number")
        a = int(input())
        c = math.sin(a)
        print("sin(",a,")", "=", c)
        s = 0
    if s == 9:
        print("Type in first number")
        a = int(input())
        c = math.cos(a)
        print("cos(",a,")", "=", c)
        s = 0
    if s == 10:
        print("Type in first number")
        a = int(input())
        c = math.tan(a)
        print("tg(",a,")", "=", c)
        s = 0

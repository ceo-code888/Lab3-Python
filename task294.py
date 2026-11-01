a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

for num in range(a, b + 1):
    s = str(num)
    # Перевірка, чи є число паліндромом
    if s[0] == s[3] and s[1] == s[2]:
        print(num)
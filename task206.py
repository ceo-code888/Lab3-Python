n = int(input("Введіть кількість предметів n: "))
total = 0

for i in range(n):
    grade = float(input(f"Введіть оцінку {i+1}: "))
    total += grade

average = total / n
print(f"Середня оцінка: {average:.2f}")
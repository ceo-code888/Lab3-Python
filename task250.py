total_sum = 0

print("Вводьте числа (0 для завершення):")
while True:
    num = int(input())
    if num == 0:
        break
    total_sum += num

print("Сума елементів:", total_sum)
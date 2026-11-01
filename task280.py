n = int(input("Введіть число n: "))

if n <= 0:
    fib = 0
elif n == 1:
    fib = 1
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    fib = b

print("Число Фібоначчі:", fib)
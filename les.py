# На вход в программу подается натуральное число n. Напишите программу,
# выводящую графическое изображение делимости чисел от 1 до n включительно.
# Вкаждой строке надо напечатать очередное число символов +, сколько делителей у этого числа
# Формат входных данных: на вход подается натуральное число n.
# Формат выходных данных: Программа должна вывести графическое изображение чисел от 1 до n,
# каждое на отдельной строке.


# A natural number n is given as input to the program. Write a program that
# displays a graphical representation of the divisibility of numbers from 1 to n, inclusive.
# In each line, print the number of + symbols corresponding to the number of divisors of that number.
# Input format: A natural number n is given as input.
# Output format: The program should display a graphical representation of the numbers from 1 to n,
# each on a separate line.


n = int(input())
for x in range (1, n+1):
    count = 0
    for i in range (1, x+1):
        if x % i == 0:
            count += 1
    print(f"{x} {'+' * count}")
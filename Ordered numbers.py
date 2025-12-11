# Дано натуральное число. Напишите программу, которая определяет, 
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
# Формат входных данных: На вход программе подаётся натуральное число.
# Формат выходных данных: Программа должна вывести «YES» (без кавычек), 
# если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию, 
# или «NO» (без кавычек) в противном случае.


# A natural number is given. Write a program that determines 
# whether the sequence of its digits, when viewed from right to left, is non-decreasing.
# Input format: The program is given a natural number as input.
# Output format: The program should output "YES" (without quotes) 
# if the sequence of its digits, when viewed from right to left, is non-decreasing, 
# or "NO" (without quotes) otherwise.

n = int(input())
prev = -1               # переменная которая гарантированно меньше любой цифры (в условии указано, что число натуральное, а значит оно не отрицательное, но тем  не менее в его составе может быть 0)
flag = True             
while n > 0:            # обработаем в цикле цифры числа справа на лево и проверим что текущая цифра не больше чем следующая, в противном случае прерываем цикл с результатом "NO"
    digit = n % 10
    if digit < prev:
        flag = False
        break
    prev = digit
    n //= 10
if flag == False:
    print("NO")
else:
    print("YES")
    
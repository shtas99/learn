# На вход программе подается два натуральных числа a и b (a < b)
# Напишите программу, которая находит натуральное число из отрезка [a; b]
# (от a до b включительно) с максимальной суммой делителей. Если числа с
# с максимальной суммой делителей несколько, то искомым числом является наибольшее
# из них. Ваша программа должна вывести ответ в следующем формате:
# <число с максимальной суммой делителей> <сумма делителей этого числа>


# The program is given two natural numbers a and b (a < b)
# Write a program that finds a natural number from the interval [a; b]
# (from a to b, inclusive) with the maximum sum of divisors. If there are multiple numbers with
# the maximum sum of divisors, then the desired number is the largest
# of them. Your program should output the answer in the following format:
# <number with the maximum sum of divisors> <sum of divisors of this number>

a = int(input())
b = int(input())
max_sum = 0
resolt_num =0


for current_num in range (a, b + 1):    # Перибираем все числа в указанном диапазоне
    current_sum = 0
    for divisor in range (1, x+1):      # Ищем делители
        if current_num % divisor == 0:
            current_sum += divisor      # Сумма делителей для текущего числа ()
    if current_sum >= max_sum:          # проверим необходимость обновить счетчик суммы делителей и число
        max_sum = current_sum
        resolt_num = current_num
print(f"{resolt_num} {max_sum}")
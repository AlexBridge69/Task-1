# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
my_list = list(range(1, 10))
print("Введите через Enter 9 чисел:")
sum = 0
for i in range(0, len(my_list)):
    my_list[i] = int(input())
    if i % 2 == 0:
        sum += my_list[i]

print(my_list)
print(f'Сумма чисел списка, стоящих на нечетной позиции равна {sum}.')
#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит 
#натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
A = []
N = int(input("Введите длину массива: "))
X = int(input("Какое число хотите найти?: "))
count = 0
for i in range(N):
    A.append(random.randint(0, 2))
    if X == A[i]:
        count += 1
print(A)
print(count)
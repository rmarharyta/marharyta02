# варіант 20
import random
import math


def secret(message, N):
    square_root = math.ceil(math.sqrt(N))
    lenght = square_root ** 2
    list = []

    for i in range(lenght):
        y = chr(ord('A') + (i % 26))
        list.append(y)
    random.shuffle(list)
    lenght2 = lenght-len(message)
    list1 = list[:lenght2]
    message = message
    message = message + ''.join(list1)
    parts = [message[i:i + N] for i in range(0, lenght, N)]

    for i in range(N):
        for part in parts:
            if i < len(part):
                print(part[i], end=' ')
        print()


n = int(input("Введіть число: "))
sms = input("Введіть повідомлення: ")
secret(sms, n)

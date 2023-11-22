# варіант 20
N = int(input("Введіть кількість слів: "))

word = []

for i in range(N):
    words = input("Введіть слово: ")
    s = str.capitalize(words)
    word.append(s)

list = []
for s in word:
    if s not in list:
        list.append(s)


list_str = " ".join(list)

print(list_str)

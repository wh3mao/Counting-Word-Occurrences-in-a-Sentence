sentence = input("Введите предложение: ").lower()
a = 0
word = input("Введите слово: ").lower()
for words in sentence.split():
    if word in words:
        a += 1


print(f"Количество слов в предложении: {a}")
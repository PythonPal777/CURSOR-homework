text = input("Введіть текст: ")
word = input("Введіть слово, яке потрібно знайти: ")

count = text.count(word)
text = text.replace(word, word.upper())

print(f"Кількість входжень слова '{word}': {count}")
print(f"Замінений текст: {text}")

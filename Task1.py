# Задание 1 .Пользователь вводит путь к папке и искомое слово. Программа ищет слово в
# папке и её подпапках. После работы программы формируется отчет с информацией
# о том, где было слово найдено, количество совпадений. Добавьте возможность замены или удаления
# искомого слова из файлов.

import os

# ищем слово в текущей директории
motherFolder = os.getcwd()
word = input('Введите искомое слово. Например, Python ')
filesWithWord = []
searchResult = False
# проходим по дочерним папкам
for root, dirs, files in os.walk(motherFolder):
    for file in files:
        # и открываем каждый текстовый файл
        if file.endswith(".txt"):
            myfile = os.path.join(root, file)
            f = open(myfile, encoding='UTF-8', mode='r')
            text = f.read()
            f.close()
            text = text.split()
            counter = 0
            # если искомое слово найдено, сохраняем путь к файлу в список для дальнейшей работы
            if word in text:
                globals()
                searchResult = True
                filesWithWord.append(myfile)
                for i in text:
                    if i == word:
                        counter += 1
                print('Слово', word, 'обнаружено в файле', file, 'директория', os.path.join(root), counter, 'раз')
if searchResult == True:
    choice = int(input(
        'Выберите действие: \n 1. Заменить искомое слово \n 2. Удалить искомое слово \n 3. Выйти из программы без сохранения'))
    if choice == 1:
        newWord = input('Введите новое слово ')
        # обращаемся к списку с путями к файлам с найденным словом
        for i in filesWithWord:
            f = open(i, encoding='UTF-8', mode='r')
            text = f.read()
            f.close()
            text = text.split()
            newText = ''
            for j in text:
                if j != word:
                    newText += j + ' '
                # заменяем найденное слово на новое
                else:
                    newText += newWord + ' '

            f = open(i, encoding='UTF-8', mode='w')
            f.write(newText)
            f.close()
    elif choice == 2:
        for i in filesWithWord:
            f = open(i, encoding='UTF-8', mode='r')
            text = f.read()
            f.close()
            text = text.split()
            newText = ''
            for j in text:
                if j != word:
                    # удаляем найденное слово
                    newText += j + ' '
                else:
                    continue

            f = open(i, encoding='UTF-8', mode='w')
            f.write(newText)
            f.close()
    elif choice == 3:
        quit()
    print('Изменения сохранены в файлы')
else:
    print('Слово не найдено')

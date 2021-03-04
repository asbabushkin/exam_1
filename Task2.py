# Задание 2
# Определить, сколько символов букв содержит файл.
# Скопировать из файла F1 в файл F2 все символы кроме символов-«цифр».
# Определить, сколько раз заданный разделитель встречается в файле.
# Скопировать из файла F1 в файл F2 все символы, заменив символ-«цифру» на символ %.

f = open('task.txt', encoding='UTF-8', mode='r')
text = f.read()
f.close()
newText = ''
newText2 = ''
letters = ('а б в г д е ё ж з и к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I G K L M N O P Q R S T U V W X Y Z')
letters = letters.split()
sep = ' '
counter = 0
sepCounter = 0


for i in text:
# считаем буквы в файле
    if i in letters:
        counter += 1
# считаем пробелы в файле
    if i == sep:
        sepCounter += 1
# удаляем цифры из файла
    if not i.isdigit():
        newText = newText + i
# заменяем цифры в файле на %
    if i.isdigit():
        i = '%'
    newText2 = newText2 + i



print('Файл содержит', counter, 'букв')
print('Файл содержит', sepCounter, 'пробелов')

newF = open('newFile.txt', encoding='UTF-8', mode= 'w')
newF.write(newText)
newF.close()
print('Все символы кроме цифр скопированы в файл newFile.txt')
newF2 = open('newFile2.txt', encoding='UTF-8', mode='w')
newF2.write(newText2)
newF2.close()
print('Все символы скопированы в файл newFile2.txt, цифры заменены на "%"')
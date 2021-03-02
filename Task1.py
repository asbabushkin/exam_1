import os
motherFolder = "D:\Python\homework\Python hw 27\Python hw 27.2\searchFolder"
word = 'Python'

for root, dirs, files in os.walk(motherFolder):
    for file in files:
        if file.endswith(".txt"):

            myfile = os.path.join(root, file)
            # print(myfile)
            f = open(myfile, encoding='UTF-8', mode='r')
            text =f.read()
            text = text.split()
            if word in text:
                print('Слово', word,'обнаружено в файле', file, 'директория', os.path.join(root) )
            # # print(os.path.join(root, file))
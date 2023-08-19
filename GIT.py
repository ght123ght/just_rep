def str_rd():
    ln = str(input('Введите слово/строку: ')).lower().strip()
    inv = ln[::-1]
    if ln == inv:
        print(True)
    else:
        print(False)

str_rd()






















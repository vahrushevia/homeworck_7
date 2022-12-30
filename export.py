import echo

def exp():
    try:
        with open('phoebook.txt', 'r', encoding='utf-8') as file:
            li = [i for i in file.readlines()]
        with open('export.txt', 'w', encoding='utf-8') as file:
            for line in li:
                file.write(f'{line}')
    except:
        echo.error(4)
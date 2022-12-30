import csv
import echo
def add_user(user):
# добавление пользователя
    try:
        # если есть файл дозаписываем
        with open('phoebook.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{user}')
        with open('phonebook.csv', 'a') as file_csv:
            writer = csv.writer(file_csv, delimiter=';')
            writer.writerows([user])
    except:
        # если нет файла создаем
        with open('phoebook.txt', 'w', encoding='utf-8') as file:
            file.write(f'{user}')
        with open('phonebook.csv', 'w') as file_csv:
            writer = csv.writer(file_csv, delimiter=';')
            writer.writerows([user])

def find_user(find):
    # поиск по файлу
    try:
        # если есть файл дозаписываем
        with open('phoebook.txt', 'r', encoding='utf-8') as file:
            li = [i for i in file.readlines() if find in i]
            # li = file.read()
        # list = []
        # bo=False
        if li!=[]:
            print('Совпадения онаружены:')
            for i in li:
                print(i)
        else:
            print('Совпадений не обнаружено')
    except:
        echo.error(3)
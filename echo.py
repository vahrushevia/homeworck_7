
# выбор действия пользователя
def choice():
    return input('Выберите действие\n \
        1. Вывод справочника\n \
        2. Добавление контакта\n \
        3. Поиск контакта\n \
        4. Экспорт контактов\n \
        5. Выход\n')

# вывод ошибок
def error(err):
    if err==1:
        print('Ошибка №1: Не корректный ввод')
    elif err==2:
        print('Ошибка №2: Справочник пока пуст, для просмотра добавте контакты')
    elif err==3:
        print('Ошибка №3: Справочник пока пуст, для поиска добавте контакты')
    elif err==4:
        print('Ошибка №4: Справочник пока пуст, для экспорта добавте контакты')

def new_user():
    return input('Введите Фамилию Имя Отчество Телефон:\n').split()

def input_find():
    return input('Введите Имя или телефон контакта для поиска:\n')

def print_phonebook():
    try:
        # если есть файл дозаписываем
        with open('phoebook.txt', 'r', encoding='utf-8') as file:
            li = [file.read()]
        for line in li:
            print(line)
        file.close()
    except:
        error(2)



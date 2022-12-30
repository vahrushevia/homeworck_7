import echo
import action
import export

def run():
    while True:
        ch = echo.choice()
        if ch == '1':
            #  1. Вывод справочника
            echo.print_phonebook()
        elif ch == '2':  
            # 2. Добавление контакта
            user = echo.new_user()
            action.add_user(user)
        elif ch == '3':
            # 3. Поиск контакта
            find =  echo.input_find()
            action.find_user(find)
        elif ch == '4':   
            # 4. Экспорт контактов
            export.exp()
        elif ch == '5':    
            # 5. Выход
            break
        else:
            # ошибка ввода
            echo.error(1)

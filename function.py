import json


phonelist = {}

def show_contact():
    print('Текущий список контактов: ')
    for key, value in phonelist.items():
        print(key, value)


def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    father_name = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    phonelist[surname] = {
        "Имя": name,
        "Отчество": father_name,
        "Номер телефона": number
    }
    print('Контакт успешно добавлен')


def import_contact():
    with open("phonelist.json", "r", encoding="utf-8") as fh:
        phonelist = json.load(fh)
    print("Справочник телефонов успешно загружен")
    return phonelist


def export_contact():
    with open("phonelist.json", "w", encoding="utf-8") as fh:
        fh.writelines(json.dumps(phonelist, ensure_ascii=False))
    print("Справочник телефонов успешно сохранен.")


def delete_contact():
    delete = input('Введите фамилию контакта, который необходимо удалить: ')
    try:
        phonelist.pop(delete)
        print('Контакт успешно удалён!')
    except:
        print('Контакт не найден!')
        

def search_contact():
    key = input('Введите фамилию контакта, который хотите найти: ')
    value = phonelist.get(key)
    
    if key in phonelist:
        print('Результат поиска:', value)
    else:
        print('Контакт не найден')


def change_contact():
    key = input('Введите фамилию контакта, который нужно изменить: ')
    value = phonelist.get(key)
    
    if key in phonelist:
        print('Изменяемый контакт:', value)
        name = input('Введите новое имя: ')
        surname = input('Введите новую фамилию: ')
        father_name = input('Введите новое отчество: ')
        number = input('Введите новый номер телефона: ')
        phonelist[surname] = {
        "Имя": name,
        "Отчество": father_name,
        "Номер телефона": number
        }
        print('Контакт успешно изменён!')
        try:
            phonelist.pop(key)
        except:
            False
    else :
        print('Контакт не найден!')

    
while True:
    command = input("Введите команду: ")
    if command == '/start':
        print('Справочник телефонов запущен. Просмотр всех команд: /help')
    elif command == '/help':
        print('Просмотр всех команд: /help' + '\n'   
        +'Просмотр всех контактов: /show' + '\n'
        +'Добавить новый контакт: /add' + '\n'
        +'Импорт контактов: /import' + '\n'
        +'Закрыть и сохранить телефонный справочник: /exit' + '\n'
        +'Поиск контакта: /search' + '\n'
        +'Удалить контакт: /delete' + '\n'
        +'Изменить контакт: /change' + '\n'
        +'Сохранить текущий список: /save')
    elif command == '/show':
        show_contact()
    elif command == '/add':
        add_contact()
    elif command == '/import':
        phonelist = import_contact()
    elif command == '/save':
        export_contact()
    elif command == '/exit':
        export_contact()
        print('Телефонный справочник закрыт.')
        break
    elif command == '/delete':
        delete_contact()
    elif command == '/search':
        search_contact()
    elif command == '/change':
        change_contact()
    else:
        print('Неопознанная команда. Посмотреть все команды /help')
